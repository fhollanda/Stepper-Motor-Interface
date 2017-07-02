from flask import Flask
from flask_restful import Resource, reqparse
import dictionaries.capturesdb as db
import util.helper as helper
import json

class CapturesList(Resource):
    def get(self):
        return {'captures': db.get_all_captures()}

class Capture(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('uuid', type = str, required = True, help = helper.CAPTURES['uuid'], location = 'json')
		self.reqparse.add_argument('fileformat', type = str, location = 'json')
		super(Capture, self).__init__()

	def get(self, uuid, fileformat = "json"):
		if fileformat in helper.FORMATS:

			return {'message': {'uuid': uuid, 'format': fileformat}}
		return {'message': helper.CAPTURES['format']}

	def delete(self, uuid):
		is_deleted = db.delete_capture(str(uuid))
		if(is_deleted):
			return {"is_deleted": is_deleted}
		else:
			return {"is_deleted": False}