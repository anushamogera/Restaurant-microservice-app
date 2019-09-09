# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
from requests import get, post, put, delete
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from project.models.Menu import Items
from bs4 import BeautifulSoup
import requests
from xml.dom import minidom
import xmltodict, json
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#class CreateForm(FlaskForm):
#    text = StringField('name', validators=[DataRequired()])


@app.route('/')
def start():
	items = Items()
	items_data = items.get_all()
	return render_template('index.htm' , items = items_data['response'])

@app.route('/about')
def about():
	return render_template('about.htm')

@app.route('/update_crawl')
def update_crawl():
	get("http://localhost:5000/crawl_portofino")
	get("http://localhost:5000/crawl_amano")
	get("http://localhost:5000/crawl_asiaresturant")
	get("http://localhost:5000/crawl_langosch")
	get("http://localhost:5000/crawl_pdf")
	return json.dumps({"response": "Data updated"})

@app.route('/crawl_portofino')
def crawl_portofino():
	resturant_name = 'Trattoria Portofino'
	email = 'info@portofino-trattoria.de '
	contact_num = '030-23910610'
	address = 'Trattoria Portofino Gubener Straße 48 10243 Berlin'
	timings = 'Montag - Sonntag: 11.30 - 24.00 Uhr'
	page  = requests.get("http://www.portofino-trattoria.de/")
	data = []
	soup = BeautifulSoup(page.text, 'html.parser')
	for link in soup.find_all("div", class_="ed-headline"):
		sub_id = link.find(class_='wv-link-elm')
		if(sub_id):
			sub_id = sub_id.get('href')
			sub_id = sub_id.replace('#','')
			category = link.get_text()
			dishes = soup.find(id=sub_id)
			for menus in dishes.find_all("tr"):
				td_list = menus.find_all("td")
				name = td_list[0].find("strong").get_text()
				desc = td_list[0].get_text()
				desc = desc.replace(name,'')
				price = td_list[1].get_text()
				info = {'name': name , 'price': price.decode("utf-8").replace(u"\u20ac", "").replace(",", ".") , 'category':category , 'description': str(desc) , 'type':'website' , 'resturant':resturant_name}
				data.append(info)
	items = Items()
	items_data = items.post(data)
	return json.dumps(data)

@app.route('/crawl_amano')
def crawl_amano():
	resturant_name = 'Amano'
	email = 'info@portofino-trattoria.de '
	contact_num = '030-23910610'
	address = 'Trattoria Portofino Gubener Straße 48 10243 Berlin'
	timings = 'Montag - Sonntag: 11.30 - 24.00 Uhr'
	data = []
	page  = requests.get("http://www.amano-ristorante.de/speisen/?lang=en")
	soup = BeautifulSoup(page.text, 'html.parser')
	for link in soup.find_all("div", class_="fw-heading-with-subtitle"):
		name = link.find("h4", class_="fw-special-title")
		if(name):
			name = name.get_text()
			price = link.find("div", class_="fw-special-subtitle").get_text()
			desc = link.find_next_sibling("div")
			if(desc):
				desc = desc.get_text()
		info = {'name': name , 'price': price.decode("utf-8").replace(u"\u20ac", "").replace(",", ".") , 'category':'' , 'description': str(desc) , 'source':'website' , 'resturant':resturant_name}
		data.append(info)
	items = Items()
	items_data = items.post(data)
	return json.dumps(data)


@app.route('/crawl_asiaresturant')
def crawl_asiaresturant():
	resturant_name = 'Hoang Do Asia'
	email = 'info@portofino-trattoria.de '
	contact_num = '030-23910610'
	address = 'Trattoria Portofino Gubener Straße 48 10243 Berlin'
	timings = 'Montag - Sonntag: 11.30 - 24.00 Uhr'
	data = []
	page  = requests.get("https://www.asiarestaurantsushibarhoangdo.de/")
	soup = BeautifulSoup(page.text, 'html.parser')
	for link in soup.find_all("div", class_="menucat"):
		category = link.find(class_='category').get_text()
		dishes = link.find(class_='zebra')
		for dish in dishes.find_all("li"):
			dish_name = dish.find('b').get_text()
			dish_price = dish.find(class_='price').get_text()
			dish_desc = dish.find('span', itemprop='description')
			if(dish_desc):
				dish_desc = dish_desc.get_text()
			info = {'name': dish_name , 'price': dish_price.decode("utf-8").replace(u"\u20ac", "").replace(",", ".") , 'category':category , 'description': str(dish_desc) , 'source':'website' , 'resturant':resturant_name}
			data.append(info)
	items = Items()
	items_data = items.post(data)
	return json.dumps(data)

@app.route('/crawl_langosch')
def crawl_langosch():
	resturant_name = 'Langosch'
	email = ''
	contact_num = ''
	address = ''
	timings =  ''
	data = []
	page  = requests.get("http://langosch-berlin.de/speisen")
	soup = BeautifulSoup(page.text, 'html.parser')
	food_items_list = soup.find("ul", class_="food-list-wrapper")
	for item in food_items_list.find_all("li"):
		category = item.find('h2').get_text()
		cat_food_list = item.find("ul", class_="food-list")
		if(cat_food_list):
			for dishes in cat_food_list.find_all("li"):
				name = dishes.find("h2", class_="menu-item-header").get_text()
				price = dishes.find("div", class_="price").get_text()
				info = {'name': name , 'price': price.decode("utf-8").replace(u"\u20ac", "").replace(",", ".") , 'category':category , 'description': '' , 'source':'website' , 'resturant':resturant_name}
				data.append(info)
	items = Items()
	items_data = items.post(data)
	return json.dumps(data)

@app.route('/crawl_pdf')
def crawl_pdf():
	mydoc = open('test.xml')
	o = xmltodict.parse(mydoc)
	data = json.dumps(o, indent=4)  
	data = json.loads(data)

	new_start = False
	new_end = False
	categories = []
	dishname = []
	dishes = []
	for p in data['pdf2xml']['page']:
		for d in p['text']:
			if(d['@height'] == '92'):
				#print d['i']
				category = d['i']
				#categories.append(d['i'])
			elif(d['@height'] == '28'):
				if 'b' in d:
					new_data = []
					data = d['b']
					for rep in data:
						update_data = rep.decode("utf-8").replace(u"\u20ac", "mera_euro")
						new_data.append(update_data)
					if '.' in d['b']:
						print "New Dish found"
						print d['b']
						new_start = True
						new_end = False
						dishname = d['b']
					elif "mera_euro" in new_data:
						print "New Dish End"
						new_start = False
						new_end = True
					#print d['b']
				if '#text' in d:
					desc = d['#text']
			info = {'name': name , 'price':'' , 'category':category , 'description': '' , 'source':'pdf' , 'resturant':'acheron'}
			data.append(info)
	items = Items()
	items_data = items.post(data)
	return json.dumps(data)

