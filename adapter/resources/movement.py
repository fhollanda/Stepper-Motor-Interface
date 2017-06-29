# encoding: utf-8

from flask_restful import Resource, reqparse
from flask import jsonify, abort
from util.request_wrapper import post_data, get_data
import util.endpoint as endpoint
import util.helper as helper
import logging
import settings

class SingleAxisMove(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('direction', type = str, required = True, help = helper.MOVE['direction'], location = 'json')
		self.reqparse.add_argument('steps', type = int, required = True, help = helper.MOVE['steps'], location = 'json')
		self.reqparse.add_argument('acquisition_rate', type = int, required = True, help = helper.MOVE['acquisition_rate'], location = 'json')
		super(SingleAxisMove, self).__init__()

	def post(self, axis):
		settings._isRunning = True
		axis_list = {"x": 4, "y": 3, "z": 1}
		
		if axis in axis_list:

			try:
				args = self.reqparse.parse_args()
				acquisition_rate = args['acquisition_rate']
				full_path = args['steps']
			except Exception as e:
				logging.error(e)
				abort(500, cause=helper.FIELDS(), error=str(e))

			response_list = []

			for i in range(0, full_path, acquisition_rate):
				data = {	'direction': args['direction'], 'steps': acquisition_rate, 'acknowledge': True 	}
				response = post_data(endpoint.movement + "/{}".format(axis_list.get(axis)), data, True)

				response_node = str(response.json()['response'])

				if response_node == "ao" or response_node == "a":
					acquired_data = get_data(endpoint.acquire + "/{}".format(1)).json()
					print("Obtendo ponto: %s" % i)
					if(acquired_data):
						response_list.append(acquired_data)
					else: 
						abort(500, message=helper.ERROR['SCOPE_EXCEPTION'])
				else: 
					abort(500, message=helper.ERROR['MOTOR_EXCEPTION'])

			return {'message': response_list}, 200
		else:
			abort(400, helper.MOVE['primary_axis'])

class DoubleAxisMove(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('primary_axis', type = str, required = True, help = helper.MOVE['primary_axis'], location = 'json')
		self.reqparse.add_argument('direction', type = str, required = True, help = helper.MOVE['direction'], location = 'json')
		self.reqparse.add_argument('steps', type = int, required = True, help = helper.MOVE['steps'], location = 'json')
		self.reqparse.add_argument('acquisition_rate', type = int, required = True, help = helper.MOVE['acquisition_rate'], location = 'json')
		self.reqparse.add_argument('secondary_axis', type = str, required = True, help = helper.MOVE['secondary_axis'], location = 'json')
		self.reqparse.add_argument('acquisition_offset_rate', type = int, required = True, help = helper.MOVE['acquisition_offset_rate'], location = 'json')
		self.reqparse.add_argument('secondary_axis_step_size', type = int, required = True, help = helper.MOVE['secondary_axis_step_size'], location = 'json')
		self.reqparse.add_argument('acquisition_channel', type = int, required = False, location = 'json')
		super(DoubleAxisMove, self).__init__()
	
	def post(self):
		settings._isRunning = True
		axis_list = {"x": 4, "y": 3, "z": 1}

		try:
			args = self.reqparse.parse_args()
			primary_axis = args['primary_axis']
			acquisition_rate = args['acquisition_rate']
			full_path = args['steps']
			direction = args['direction']
			secondary_axis = args['secondary_axis']
			acquisition_offset = args['acquisition_offset_rate']
			secondary_axis_step_size = args['secondary_axis_step_size']
			acquisition_channel = args['acquisition_channel']
		except Exception as e:
			logging.error(e)
			abort(500, cause=helper.FIELDS(), error=str(e))

		response_list = []

		for i in range(0, acquisition_offset):
			if i > 0:
				data = {	'direction': direction, 'steps': secondary_axis_step_size, 'acknowledge': True 	}
				offset_response = post_data(endpoint.movement + "/{}".format(axis_list.get(secondary_axis)), data, True)
				offset_response_node = str(offset_response.json()['response'])

				if offset_response_node == "ao" or offset_response_node == "a":
					response_list.append([])

					reverse_direction = get_reverse_direction(direction)

					return_data = {	'direction': reverse_direction, 'steps': full_path, 'acknowledge': True }
					response = post_data(endpoint.movement + "/{}".format(axis_list.get(primary_axis)), return_data, True)
				else:
					abort(500, message=helper.ERROR['MOTOR_EXCEPTION'])
			else:
				response_list.append([])

			for j in range(0, full_path, acquisition_rate):
				data = {	'direction': direction, 'steps': acquisition_rate, 'acknowledge': True 	}
				response = post_data(endpoint.movement + "/{}".format(axis_list.get(primary_axis)), data, True)
				
				response_node = str(response.json()['response'])

				if response_node == "ao" or response_node == "a":
					acquired_data = get_data(endpoint.acquire + "/{}".format(1)).json()
					print("Obtendo ponto: %s" % j)
					if(acquired_data):
						response_list[i].append(acquired_data)
					else: 
						abort(500, message=helper.ERROR['SCOPE_EXCEPTION'])
				else: 
					abort(500, message=helper.ERROR['MOTOR_EXCEPTION'])

		return {'message': response_list}, 200

def get_reverse_direction(direction):
	if direction == "f":
		return "r"
	elif direction == "r":
		return "f"