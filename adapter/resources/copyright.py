from flask_restful import Resource
from flask import jsonify
from util.request_wrapper import get_response
import util.endpoint as endpoint

class Copyright(Resource):
    def get(self):
    	return get_response(endpoint.copyright)