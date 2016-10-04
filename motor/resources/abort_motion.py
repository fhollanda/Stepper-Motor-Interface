from flask_restful import Resource, reqparse
from util.serial_processor import send_and_receive_data
import util.commands as commands

class AbortMotion(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('get_steps_taken', type = bool, required = False, location = 'json')
		super(AbortMotion, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		get_steps_taken = args['get_steps_taken']

		serial_return = do_abort(get_steps_taken)
		return {'response': serial_return[1]}, serial_return[0]

def do_abort(get_steps_taken):
	if(get_steps_taken):
		return send_and_receive_data(commands.ABORT, "", "rt") 
	else: 
		return send_and_receive_data(commands.ABORT)