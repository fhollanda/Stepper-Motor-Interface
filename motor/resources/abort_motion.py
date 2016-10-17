from flask_restful import Resource, reqparse
from util.serial_processor import send_c4_command, send_single_command
import util.commands as commands

class AbortMotion(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('request_position', type = bool, required = False, location = 'json')
		super(AbortMotion, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		get_steps_taken = args['request_position']

		serial_return = do_abort(get_steps_taken)
		return {'response': serial_return[1]}, serial_return[0]

def do_abort(get_steps_taken):
	if(get_steps_taken):
		send_c4_command(command, False)
		motor_position_response = send_single_command(commands.REQUEST_MOTOR_POSITION + commands.CR)
		return motor_position_response
	else: 
		return send_c4_command(commands.ABORT)