from flask import Flask, make_response, send_from_directory
from flask_restful import Resource, reqparse
import dictionaries.capturesdb as db
import util.helper as helper
import util.filemanager as filemg
import json, logging, ast, re, numpy
import scipy.io as sio

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
			file = get_file(str(uuid))
			if(file):
				json_file = ast.literal_eval(json.loads(file))

				if(json_file):
					if(is_matlab(fileformat)):
						try:
							only_data = json_file['acquired_data']
							only_array = get_only_values(only_data)
							filepath = filemg.captures_path +'temp.mat'
							sio.savemat(filepath, mdict={'acquired_data':only_array})

							if(filemg.check(filepath)):
								response = make_response(send_from_directory(filemg.captures_path, 'temp.mat'))
								response.headers['Content-Type'] = 'application/octet-stream'
								return response
						except Exception as e:
							logging.exception(e)
					else:
						return {'file': json_file}
			else:
				return {'message': helper.CAPTURES['file'].format(uuid, fileformat)}
		return {'message': helper.CAPTURES['format']}

	def delete(self, uuid):
		is_deleted = del_file_and_dict(str(uuid))
		if(is_deleted):
			return {"is_deleted": is_deleted}
		else:
			return {"is_deleted": False}

def get_only_values(data_list):
	returnable = []

	if(has_items(data_list)):
		for i in range(0, len(data_list)):
			for key, value in data_list[i].items():
				returnable.append(ast.literal_eval(value))
	else:
		for i in range(0, len(data_list)):
			returnable.append([])
			for j in range(0, len(data_list[i])):
				for key, value in data_list[i][j].items():
					returnable[i].append(ast.literal_eval(value))

	return returnable

def has_items(data):
	try:
		return data[0].items() 
	except Exception as e:
		return False

def del_file_and_dict(key):
	try:
		filepath = filemg.captures_path + key
		file_exists = filemg.check(filepath) and db.has_key(key)
		if file_exists:
			filemg.delete(filepath)
			db.delete_capture(key)
			return True
		else:
			return False
	except Exception as e:
		logging.exception(e)
		return False

def get_file(key):
	try:
		filepath = filemg.captures_path + key
		file_exists = filemg.check(filepath) and db.has_key(key)
		if file_exists:
			return filemg.load(filepath)
	except Exception as e:
		logging.exception(e)

def is_matlab(string):
	return string.lower() == "matlab"
