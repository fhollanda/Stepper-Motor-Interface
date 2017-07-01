from flask_restful import Resource, reqparse
from flask import abort
from util.request_wrapper import post_data
import util.endpoint as endpoint

class SetScopeConfig(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('channel', type = int, required = False, location = 'json')
		self.reqparse.add_argument('frequency', type = int, required = False, location = 'json')
		self.reqparse.add_argument('cycles', type = int, required = False, location = 'json')
		self.reqparse.add_argument('averaging', type = int, required = False, location = 'json')
		self.reqparse.add_argument('v_scale', type = float, required = False, location = 'json')
		self.reqparse.add_argument('t_scale', type = float, required = False, location = 'json')
		super(SetScopeConfig, self).__init__()

	def post(self):
		try:
			args = self.reqparse.parse_args()
			channel = args['channel']
			frequency = args['frequency']
			cycles = args['cycles']
			averaging = args['averaging']
			v_scale = args['v_scale']
			t_scale = args['t_scale']
		except Exception as e:
			abort(500)

		data = { 
			'channel': channel,
			'frequency': frequency,
			'cycles': cycles,
			'averaging': averaging,
			'v_scale': float(v_scale),
			't_scale': float(t_scale) 
		}

		return post_data(endpoint.scope_config, data).json()