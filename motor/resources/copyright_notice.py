from flask_restful import Resource
from util.serial_write import do_command

class CheckCopyright(Resource):
    def get(self):
    	serial_return = do_command("(c)")
        return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}