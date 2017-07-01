from flask_restful import Resource
from util.request_wrapper import get_data
import util.endpoint as endpoint

class Copyright(Resource):
	def get(self):
		return get_data(endpoint.copyright).json()