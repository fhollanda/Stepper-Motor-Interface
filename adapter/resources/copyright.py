from flask_restful import Resource
from flask import jsonify
from util.status_response import show_message_for
import util.endpoints as endpoint
import requests

class Copyright(Resource):
    def get(self):
    	response = requests.request("GET", endpoint.get_copyright)
    	status_code = response.status_code

    	if(status_code == requests.codes.ok):
    		return response.json()
        else:
        	return show_message_for(status_code), status_code