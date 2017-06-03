from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask("driver_mock")
CORS(app)

@app.before_request
def only_json():
    if request.data and not request.is_json: 
        abort(400)

api = Api(app)

class CaptureWaveform(Resource):
	def __init__(self):
		super(CaptureWaveform, self).__init__()

	def get(self, id = None):
		return {'data': "[[0, 1], [2, 3]]"}, 200

class ConfigureScopeParams(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('channel', type = int, required = False, location = 'json')
		self.reqparse.add_argument('frequency', type = int, required = False, location = 'json')
		self.reqparse.add_argument('cycles', type = int, required = False, location = 'json')
		self.reqparse.add_argument('averaging', type = int, required = False, location = 'json')
		self.reqparse.add_argument('v_scale', type = float, required = False, location = 'json')
		self.reqparse.add_argument('t_scale', type = float, required = False, location = 'json')
		self.reqparse.add_argument('save_data', type = bool, required = False, location = 'json')
		super(ConfigureScopeParams, self).__init__()

	def post(self):
		return {'data': "OK"}, 200

api.add_resource(CaptureWaveform, '/oscilloscope/api/acquire')
api.add_resource(ConfigureScopeParams, '/oscilloscope/api/config')

if __name__ == '__main__':
	app.run(debug=True, port=5003)