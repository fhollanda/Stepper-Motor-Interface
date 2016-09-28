from flask_restful import Resource, reqparse
from util.serial_write import serial_process
import util.commands as commands

class MoveMotor(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('direction', type = str, required = True, help = 'No direction provided', location = 'json')
		self.reqparse.add_argument('motorNumber', type = int, required = True, help = 'No motorNumber provided', location = 'json')
		self.reqparse.add_argument('steps', type = int, required = True, help = 'No steps provided', location = 'json')
		super(MoveMotor, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		direction = args['direction']
		motorNumber = args['motorNumber']
		steps = args['steps']

		serial_return = do_movement(direction, motorNumber, steps)
		return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}

def do_movement(direction, motorNumber, steps):
	parameters = str(motorNumber) + direction + str(steps)
	return serial_process(commands.MOVE, parameters)