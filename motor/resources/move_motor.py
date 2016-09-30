from flask_restful import Resource, reqparse
from util.serial_processor import send_and_receive_data
import util.commands as commands

class MoveMotor(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('direction', type = str, required = True, help = 'No direction provided', location = 'json')
		self.reqparse.add_argument('motor_number', type = int, required = True, help = 'No motor_number provided', location = 'json')
		self.reqparse.add_argument('steps', type = int, required = True, help = 'No steps provided', location = 'json')
		self.reqparse.add_argument('acknowledge', type = bool, required = False, location = 'json')
		super(MoveMotor, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		direction = args['direction']
		motor_number = args['motor_number']
		acknowledge = args['acknowledge']
		steps = args['steps']

		serial_return = do_movement(direction, motor_number, steps, acknowledge)
		return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}

def do_movement(direction, motor_number, steps, acknowledge):
	acknowledgeFlag = "n" if(acknowledge) else ""
	pre_parameters = str(motor_number) + direction + str(steps) + acknowledgeFlag
	return send_and_receive_data(commands.MOVE, pre_parameters)