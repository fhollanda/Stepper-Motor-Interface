from flask_restful import Resource
from util.serial_write import serial_process
import util.commands as commands

class CheckCopyright(Resource):
    def get(self):
    	serial_return = serial_process(commands.MOVE)
        return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}