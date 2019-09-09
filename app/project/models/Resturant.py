# -*- coding: utf-8 -*-
from flask import jsonify
from requests import get, post, put, delete

class Resturant(object):
    def get_all(self):
    	data = get("http://localhost:5000/Menus/")
    	return jsonify(data.json())
        
