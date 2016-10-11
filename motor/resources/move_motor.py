from flask_restful import Resource, reqparse
from util.serial_processor import send_c4_command, send_single_command
import util.commands as commands

class MoveMotor(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('direction', type = str, required = True, help = 'No direction provided', location = 'json')
		self.reqparse.add_argument('steps', type = int, required = True, help = 'No steps provided', location = 'json')
		self.reqparse.add_argument('acknowledge', type = bool, required = False, location = 'json')
		super(MoveMotor, self).__init__()

	def post(self, id):
		args = self.reqparse.parse_args()
		direction = args['direction']		
		steps = args['steps']
		acknowledge = args['acknowledge']

		serial_return = do_single_movement(id, direction, steps, acknowledge)
		return {'response': serial_return[1]}, serial_return[0]

def do_single_movement(motor_number, direction, steps, acknowledge):
	acknowledge_flag = "n" if(acknowledge) else ""
	pre_parameters = str(motor_number) + direction + str(steps) + acknowledge_flag
	return send_c4_command(commands.MOVE, pre_parameters)

class MoveMotorList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('axis', type = int, required = True, help = 'Inform how many axis will be moved, or use single move', location = 'json')
		self.reqparse.add_argument('motor_number_list', required = True, help = 'No motor_number provided', action='append')
		self.reqparse.add_argument('direction_list', required = True, help = 'No direction provided', action='append')
		self.reqparse.add_argument('steps_list', required = True, help = 'No steps provided', action='append')
		self.reqparse.add_argument('acknowledge', type = bool, required = False, location = 'json')
		super(MoveMotorList, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		axis = args['axis']
		motor_number_list = args['motor_number_list']
		direction_list = args['direction_list']
		steps_list = args['steps_list']
		acknowledge = args['acknowledge']		

		parameters = ""

		try:
			for i in range(0, axis):
				parameters += commands.MOVE + str(motor_number_list[i]) + str(direction_list[i]) + str(steps_list[i])
		except IndexError as ie: 
			return {'response': ("Please, check if every list (motor, direction and steps) has %d elements" %axis)}, 422

		serial_return = do_multiaxis_movement(parameters, acknowledge)
		return {'response': serial_return[1]}, serial_return[0]

def do_multiaxis_movement(pre_parameters, acknowledge):
	if(pre_parameters):
		pre_parameters += "n" if(acknowledge) else ""
		return send_c4_command(pre_parameters)
	else:
		return [422, "No movements information has been given, command ignored"]

class RequestMotorPosition(Resource):
	def get(self):
		serial_return = send_single_command(commands.REQUEST_MOTOR_POSITION)
		return {'response': serial_return[1]}, serial_return[0]