from flask_restful import Resource
from flask import abort
import settings

class Abort(Resource):
	def post(self):
		try:
			settings.end_run()
			return {'message': 'OK'}, 200
		except Exception as e:
			return e, 500