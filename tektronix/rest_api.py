import tds2024Cusb
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS
import time, logging

app = Flask("driver")
CORS(app)

@app.before_request
def only_json():
	if request.data and not request.is_json: 
		abort(400)

api = Api(app)

def save_data_file(data):
	ts = time.time()
	f = open( 'data/data_'+ str(ts).replace(".","") +'.temp', 'w' )
	f.write( 'data = ' + repr(data) + '\n' )
	f.close()

class CaptureWaveform(Resource):
	def __init__(self):
		super(CaptureWaveform, self).__init__()

	def get(self):
		try:
			data = channel_to_acquire.get_waveform()
		except Exception as e:
			logging.exception(e)
			abort(500, cause=str(e), error=("Couldn't acquire data from {}".format(channel_to_acquire)))

		if(DEFAULT_SAVE_DATA):
			save_data_file(data)

		return {'data': data}, 200

class ConfigureScopeParams(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('channel', type = int, required = True, help = "Post used channel", location = 'json')
		self.reqparse.add_argument('frequency', type = int, required = False, location = 'json')
		self.reqparse.add_argument('cycles', type = int, required = False, location = 'json')
		self.reqparse.add_argument('averaging', type = int, required = False, location = 'json')
		self.reqparse.add_argument('v_scale', type = float, required = False, location = 'json')
		self.reqparse.add_argument('t_scale', type = float, required = False, location = 'json')
		self.reqparse.add_argument('save_data', type = bool, required = False, location = 'json')
		super(ConfigureScopeParams, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		post_channel = args['channel']
		frequency = args['frequency']
		cycles = args['cycles']
		averaging = args['averaging']
		v_scale = args['v_scale']
		t_scale = args['t_scale']
		save_data = args['save_data']

		try:
			selected_channel = get_channel_by_number(post_channel or DEFAULT_CHANNEL)

			global channel_to_acquire
			channel_to_acquire = selected_channel

			scope.set_hScale(frequency=(frequency or DEFAULT_FREQUENCY), cycles=(cycles or DEFAULT_CYCLES))    	
			scope.set_averaging((averaging or DEFAULT_AVERAGING))

			selected_channel.set_vScale((v_scale or DEFAULT_V_SCALE))   
			selected_channel.set_tScale((t_scale or DEFAULT_T_SCALE))
			selected_channel.set_waveformParams(DEFAULT_ENCODING)			
		except Exception as e:
			logging.exception(e)
			abort(500, cause=str(e), error=("Couldn't send config data"))                  		

		return {'data': "OK"}, 200


api.add_resource(CaptureWaveform, '/oscilloscope/api/acquire')
api.add_resource(ConfigureScopeParams, '/oscilloscope/api/config')

def definition():
	global DEFAULT_CHANNEL
	global DEFAULT_FREQUENCY
	global DEFAULT_CYCLES
	global DEFAULT_AVERAGING
	global DEFAULT_V_SCALE
	global DEFAULT_T_SCALE
	global DEFAULT_SAVE_DATA
	global DEFAULT_ENCODING

	global scope
	global channel1
	global channel2
	global channel3
	global channel4	

	global channel_to_acquire

	DEFAULT_CHANNEL = 1
	DEFAULT_FREQUENCY = 1000000
	DEFAULT_CYCLES = 1
	DEFAULT_AVERAGING = 64
	DEFAULT_V_SCALE = 0.02
	DEFAULT_T_SCALE = 0.0000025
	DEFAULT_SAVE_DATA = False
	DEFAULT_ENCODING = 'RPBinary'

	try: 
		scope = tds2024Cusb.tek2024('/dev/usbtmc0')
	except Exception as e:
		logging.exception(e)
		raise

	try:
		channel1 = tds2024Cusb.channel(scope, 1)
		channel2 = tds2024Cusb.channel(scope, 2)
		channel3 = tds2024Cusb.channel(scope, 3)
		channel4 = tds2024Cusb.channel(scope, 4)
	except Exception as e:
		logging.exception(e)

	channel_to_acquire = get_channel_by_number(DEFAULT_CHANNEL)

def get_channel_by_number(channel_number):
	return {
		1: channel1,
		2: channel2,
		3: channel3,
		4: channel4,
	}.get(channel_number, channel1) 

if __name__ == '__main__':
	definition()
	channel_to_acquire.set_waveformParams(DEFAULT_ENCODING)
	app.run(debug=True, port=5003)
