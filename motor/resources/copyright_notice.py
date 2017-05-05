from flask_restful import Resource
from util.serial_processor import send_c4_command
import util.commands as commands

class CheckCopyright(Resource):
	def get(self):
		serial_return = send_c4_command(commands.COPYRIGHT)
		return {'response': serial_return}, 200