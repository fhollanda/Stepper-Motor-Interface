from flask_restful import Resource
from flask import jsonify
from util.request_wrapper import post_data
import util.endpoint as endpoint

class SetScopeConfig(Resource):
	def post(self):
		return post_data(endpoint.scope_config).json()