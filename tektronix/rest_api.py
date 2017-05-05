import tds2024Cusb
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS
import time

app = Flask("driver")
CORS(app)

@app.before_request
def only_json():
	if request.data and not request.is_json: 
		abort(400)

api = Api(app)

def save_data_file(data):
	ts = time.time()
	f = open( 'data_'+ str(ts).replace(".","") +'.py', 'w' )
	f.write( 'data = ' + repr(data) + '\n' )
	f.close()

class CaptureWaveform(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('channel', type = int, required = False, location = 'json')
		self.reqparse.add_argument('frequency', type = int, required = False, location = 'json')
		self.reqparse.add_argument('cycles', type = int, required = False, location = 'json')
		self.reqparse.add_argument('averaging', type = int, required = False, location = 'json')
		self.reqparse.add_argument('v_scale', type = int, required = False, location = 'json')
		self.reqparse.add_argument('t_scale', type = int, required = False, location = 'json')
		self.reqparse.add_argument('save_data', type = bool, required = False, location = 'json')
		super(CaptureWaveform, self).__init__()

	def get(self):
		scope.set_hScale(frequency=DEFAULT_FREQUENCY, cycles=DEFAULT_CYCLES)    	
		scope.set_averaging(DEFAULT_AVERAGING)

		channel1.set_vScale(DEFAULT_V_SCALE)                      		
		channel1.set_tScale(DEFAULT_T_SCALE)
		channel1.set_waveformParams(DEFAULT_ENCODING)

		data = channel1.get_waveform()

		if(DEFAULT_SAVE_DATA):
			save_data_file(data)

		return {'data': data}, 200

	def post(self):
		args = self.reqparse.parse_args()
		channel = args['channel']
		frequency = args['frequency']
		cycles = args['cycles']
		averaging = args['averaging']
		v_scale = args['v_scale']
		t_scale = args['t_scale']
		save_data = args['save_data']

		channel = get_channel_by_number(channel or DEFAULT_CHANNEL)

		scope.set_hScale(frequency=(frequency or DEFAULT_FREQUENCY), cycles=(cycles or DEFAULT_CYCLES))    	
		scope.set_averaging((averaging or DEFAULT_AVERAGING))

		channel.set_vScale((v_scale or DEFAULT_V_SCALE))   
		channel.set_tScale((t_scale or DEFAULT_T_SCALE))
		channel1.set_waveformParams(DEFAULT_ENCODING)                   		

		data = channel.get_waveform()

		if((save_data or DEFAULT_SAVE_DATA)):
			save_data_file(data)

		return {'data': data}, 200

api.add_resource(CaptureWaveform, '/oscilloscope/api/acquire')

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

	DEFAULT_CHANNEL = 1
	DEFAULT_FREQUENCY = 1000000
	DEFAULT_CYCLES = 2
	DEFAULT_AVERAGING = 64
	DEFAULT_V_SCALE = 0.1
	DEFAULT_T_SCALE = 0.000001
	DEFAULT_SAVE_DATA = True
	DEFAULT_ENCODING = 'RPBinary'

	try: 
		scope = tds2024Cusb.tek2024('/dev/usbtmc0')
	except Exception as e:
		abort(503, message=str(e))

	channel1 = tds2024Cusb.channel(scope, 1)
	channel2 = tds2024Cusb.channel(scope, 2)
	channel3 = tds2024Cusb.channel(scope, 3)
	channel4 = tds2024Cusb.channel(scope, 4)

def get_channel_by_number(channel_number):
	switcher = {
		1: channel1,
		2: channel2,
		3: channel3,
		4: channel4,
	}

	try:
		return switcher[channel_number]()
	except KeyError, e:
		return switcher[DEFAULT_CHANNEL]()

if __name__ == '__main__':
	definition()
	app.run(debug=True, port=5003)