from flask_restful import Resource
from flask import jsonify
import requests
import util.endpoint as endpoint

class Copyright(Resource):
    def get(self):
    	response = requests.request("GET", endpoint.get_copyright)
        return response.json(), response.status_code