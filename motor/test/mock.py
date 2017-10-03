#!motor/env/bin/python
from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask("motor_mock")
CORS(app)

@app.before_request
def only_json():
    if request.data and not request.is_json: 
        abort(400)

api = Api(app)

class MoveMotor(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('direction', type = str, required = False, location = 'json')
		self.reqparse.add_argument('steps', type = int, required = False, location = 'json')
		self.reqparse.add_argument('acknowledge', type = bool, required = False, location = 'json')
		super(MoveMotor, self).__init__()

	def post(self, id):
		return {'response': "a"}, 200

class CheckCopyright(Resource):
	def __init__(self):
		super(CheckCopyright, self).__init__()

	def get(self):
		return {'response': "OFFLINE"}, 200

api.add_resource(MoveMotor, '/motor/api/move/<int:id>')
api.add_resource(CheckCopyright, '/motor/api/copyright')

if __name__ == '__main__':
	app.run(debug=True, port=5000)