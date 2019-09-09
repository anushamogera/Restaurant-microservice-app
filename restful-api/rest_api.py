from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restplus import Api, Resource, fields
import json
from bson import ObjectId
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config["MONGO_DBNAME"] = "project_db"
app.config["MONGO_HOST"] = "mongo"
mongo = PyMongo(app, config_prefix='MONGO')
#APP_URL = "http://0.0.0.0:5000"
api = Api(app, version='0.1.0', title='Project API',
    description='This API handles the CRUD operations',
)


rns = api.namespace('Resturants', description='Resturant Data')
mns = api.namespace('Menus', description='Menu Data')

resturant_parser = api.parser()
resturant_parser.add_argument('name', type=str, required=True, help='Name', location='form')
resturant_parser.add_argument('address', type=str, required=True, help='Address', location='form')
resturant_parser.add_argument('phone', type=str, required=True, help='Phone #', location='form')
resturant_parser.add_argument('website', type=str, required=True, help='Website', location='form')
resturant_parser.add_argument('hours', type=str, required=True, help='Opening Hours', location='form')


menu_parser = api.parser()
menu_parser.add_argument('name', type=str, required=True, help='Dish Name', location='form')
menu_parser.add_argument('description', type=str, required=True, help='Description', location='form')
menu_parser.add_argument('price', type=float, required=True, help='Price', location='form')
menu_parser.add_argument('category', type=str, required=True, help='Category', location='form')
menu_parser.add_argument('type', type=str, required=True, help='Type', location='form')
menu_parser.add_argument('resturant', type=str, required=False, help='Resturant ID', location='form')

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Resturant(object):
    def __init__(self):
        with app.app_context():
            mongo.db.seqs.insert({'collection' : 'resturant_collection','id' : 0})

    def get_one(self, id):
        data = []
        resturant_info = mongo.db.resturant.find_one({"_id": str(id)})
        if resturant_info:
            return jsonify({"status": "ok", "data": resturant_info})
        else:
            return {"response": "no resturant found for {}".format(id)}

    def get_all(self):
        data = []
        if 'search' in request.args:
            query = request.args['search']
            query = query.split(',')
            if(len(query) == 3 and len(query[2]) > 0):
                if(query[1] == 'like'):
                    cursor = mongo.db.resturant.find({query[0]:query[2]}).limit(10)
                elif(query[1] == 'contains'):
                    cursor = mongo.db.resturant.find({query[0]:{"$regex": query[2]}}).limit(10)
                else:
                    return jsonify({"response": "Invalid operation.Please check again"})
                
                for resturant in cursor:
                    print resturant
                    #resturant['url'] = APP_URL + url_for('resturants') + "/" + resturant.get('name')
                    data.append(resturant)
                return jsonify({"response": data})
            else:
                return jsonify({"response": "Invalid querry.Please check again"})
        else:
            cursor = mongo.db.resturant.find({}).limit(10)
            for resturant in cursor:
                print resturant
                #resturant['url'] = APP_URL + url_for('resturants') + "/" + resturant.get('name')
                data.append(resturant)
            return jsonify({"response": data})

       
    def create(self, data):
        #data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            name = data.get('name')
            if name:
                if mongo.db.resturant.find_one({"name": name}):
                    return {"response": "Resturant name already exists."}
                else:
                    self.insert_doc(data)
                    return jsonify({"response": "Data inserted Successfully!!"})
            else:
                return {"response": "something missing.Please try again!!!"}

    def update(self, id , data):
        if data:
            mongo.db.resturant.update({'_id': str(id)}, {'$set': data})
            return jsonify({"status": "ok", "response": "Data updated Successfully!!"})
        else:
            return jsonify({"status": "ok", "response": "Data not found.Please try again!!"})

    def delete(self, record_id):
        result = mongo.db.resturant.remove({"_id": str(record_id)})
        print result
        return jsonify({"status": "ok", "response": "Data deleted Successfully!!"}) 

    def insert_doc(self,doc):
        doc['_id'] = str(mongo.db.seqs.find_and_modify(
            query={ 'collection' : 'resturant_collection' },
            update={'$inc': {'id': 1}},
            fields={'id': 1, '_id': 0},
            new=True 
        ).get('id'))

        try:
            mongo.db.resturant.insert(doc)

        except pymongo.errors.DuplicateKeyError as e:
            insert_doc(doc) 

class Menu(object):
    def __init__(self):
        with app.app_context():
            mongo.db.seqs.insert({'collection' : 'menu_collection','id' : 0})

    def get_distinct_categories(self):
        data = []
        menu_info = mongo.db.menu.find().distinct('category')
        if menu_info:
            for menu in menu_info:
                data.append(menu)
            return jsonify({"response": data})
        else:
            return jsonify({"response": "no data found"})

    def get_distinct_resturants(self):
        data = []
        menu_info = mongo.db.menu.find().distinct('resturant')
        if menu_info:
            for menu in menu_info:
                data.append(menu)
            return jsonify({"response": data})
        else:
            return jsonify({"response": "no data found"})

    def get_one(self, id):
        data = []
        menu_info = mongo.db.menu.find_one({"_id": id})
        if menu_info:
            return jsonify({"status": "ok", "data": menu_info})
        else:
            return {"response": "no menu found for {}".format(id)}

    def get_all(self):
        data = []
        if 'search' in request.args:
            query = request.args['search']
            query = query.split(',')
            if(len(query) == 3 and len(query[2]) > 0):
                if(query[1] == 'like'):
                    cursor = mongo.db.menu.find({query[0]:query[2]},{"_id":0}).sort('price', 1)
                elif(query[1] == 'contains'):
                    cursor = mongo.db.menu.find({query[0]:{"$regex": query[2]}},{"_id":0}).sort('price', 1)
                else:
                    return jsonify({"response": "Invalid operation.Please check again"})
                
                for menu in cursor:
                    print menu
                    data.append(menu)
                return jsonify({"response": data})
            else:
                return jsonify({"response": "Invalid querry.Please check again"})
        elif 'order_by' in request.args:
            query = request.args['order_by']
            query = query.split(',')
            if(len(query) == 2 and len(query[1]) > 0):
                if(query[1] == 'asc'):
                    cursor = mongo.db.menu.find({},{"_id":0}).sort(query[0], 1)
                elif(query[1] == 'desc'):
                    cursor = mongo.db.menu.find({},{"_id":0}).sort(query[0], -1)
                else:
                    return jsonify({"response": "Invalid operation.Please check again"})
                for menu in cursor:
                    print menu
                    data.append(menu)
                return jsonify({"response": data})
            else:
                return jsonify({"response": "Invalid querry.Please check again"})
        else:
            cursor = mongo.db.menu.find({},{"_id":0})
            for menu in cursor:
                data.append(menu)
            return jsonify({"response": data})
       
    def create(self, data):
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            name = data['name']
            resturant = data['resturant']
            if name and resturant:
                if mongo.db.menu.find_one({"name": name , "resturant": resturant}):
                    return {"response": "Menu already exists."}
                else:
                    self.insert_doc(data)
                    return jsonify({"response": "Data inserted Successfully!!"})
            else:
                return {"response": "Required Field missing"}

    def update(self, id,data):
        if data:
            mongo.db.menu.update({'_id': str(id)}, {'$set': data})
            return jsonify({"status": "ok", "response": "Data updated Successfully!!"})
        else:
            return jsonify({"status": "ok", "response": "Data not found.Please try again!!"})

    def delete(self, id):
        mongo.db.menu.remove({_id: str(id)})
        return jsonify({"status": "ok", "response": "Data deleted Successfully!!"}) 

    def get_by_search(self, name):
        data = []
        cursor = mongo.db.menu.find({"$text": {"$search": name}})
        for menu in cursor:
            data.append(menu)
        print data
        return jsonify({"response": data}) 

    def insert_doc(self,doc):
        doc['_id'] = str(mongo.db.seqs.find_and_modify(
            query={ 'collection' : 'menu_collection' },
            update={'$inc': {'id': 1}},
            fields={'id': 1, '_id': 0},
            new=True 
        ).get('id'))

        try:
            mongo.db.menu.insert(doc)
            mongo.db.menu.create_index([('name', 'text')])
            mongo.db.menu.create_index([('description', 'text')])

        except pymongo.errors.DuplicateKeyError as e:
            insert_doc(doc)

resturant = Resturant()
menu = Menu()

@rns.route('/')
class ResturantList(Resource):
    '''Shows a list of all Demonstrators, and lets you POST to add new Demonstrators'''
    @rns.doc('list_resturant')
    def get(self):
        '''List all Resturant'''
        return resturant.get_all()

    @api.doc(parser=resturant_parser)
    def post(self):
        '''Create a Resturant'''
        args = resturant_parser.parse_args()
        return resturant.create(args)

@rns.route('/<int:id>')
class Resturant(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @rns.doc('get_resturant_by_id')
    def get(self,id):
        '''List Resturant by id'''
        return resturant.get_one(id)

    @api.doc(parser=resturant_parser)
    def put(self, id):
        '''Update a Resturant record'''
        args = resturant_parser.parse_args()
        return resturant.update(id,args)

    @rns.doc('delete_resturant_by_id')
    def delete(self,id):
        '''delete resturant by id'''
        return resturant.delete(id)

@mns.route('/')
class MenuList(Resource):
    '''Shows a list of all Demonstrators, and lets you POST to add new Demonstrators'''
    @mns.doc('list_menu')
    def get(self):
        '''List all Menus'''
        return menu.get_all()

    @api.doc(parser=menu_parser)
    def post(self):
        '''Create a Menu'''
        args = menu_parser.parse_args()
        return menu.create(args)

@mns.route('/<int:id>')
class Menu(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @mns.doc('get_resturant_by_id')
    def get(self,id):
        '''List menu by id'''
        return menu.get_one(id)


    @api.doc(parser=resturant_parser)
    def put(self, id):
        '''Update a Menu record'''
        args = menu_parser.parse_args()
        return menu.update(id,args)

    @mns.doc('delete_resturant_by_id')
    def delete(self,id):
        '''delete menu by id'''
        return menu.delete(id)

@mns.route('/all_resturant')
class MenuResturant(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @mns.doc('get_all_resturant')
    def get(self):
        '''List all resturant in menu'''
        return menu.get_distinct_resturants()

@mns.route('/all_category')
class MenuCategory(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @mns.doc('get_all_catrgories')
    def get(self):
        '''List all categories in menu'''
        return menu.get_distinct_categories()


@mns.route('/search/<name>')
class MenuSearch(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @mns.doc('get_by_search')
    def get(self,name):
        '''search in menu'''
        return menu.get_by_search(name)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

