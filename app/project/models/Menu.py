# -*- coding: utf-8 -*-


from flask import jsonify
from requests import get, post, put, delete
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Items(object):

    def get_all(self):
    	data = get("http://api:5000/Menus/")
    	return data.json()

    def post(self,data):
    	for p in data:
    		name =  p['name']
    		cat = p['category']
    		desc = ''
    		price = p['price']
    		rest = p['resturant']
    		cmd = 'curl -X POST "http://api:5000/Menus/" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "category='+cat+'&name='+name+'&price='+price+'&resturant='+rest+'&type=website&description='+desc+'"'
    		os.system(cmd)
    	#return result.json()
        
