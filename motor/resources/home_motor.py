from flask_restful import Resource, reqparse
from util.serial_processor import send_and_receive_data, abort_home_command
import util.commands as commands

class HomeMotor(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser() 
		self.reqparse.add_argument('motor_list', type=int, action='append')

	def post(self):
		args = self.reqparse.parse_args()
		motor_list = args['motor_list']

		serial_return = do_return_home(motor_list)
		return {'serial_status': serial_return[0], 'serial_response': serial_return[1]} 

class AbortHomeCommand(Resource):
	def post(self):
		serial_return = abort_home_command()
		return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}

def do_return_home(motor_list):
	if(motor_list):
		motors = ""
		for motor in motor_list:
			motors+=str(motor)
		return send_and_receive_data(commands.HOME, motors) 
	else: 
		return send_and_receive_data(commands.HOME)