from flask_restful import Resource
from util.serial_processor import send_c4_command
import util.commands as commands


class FirmwareInformation(Resource):
	def get(self):
		product_info = send_c4_command(commands.FIRMWARE_INFO_PRODUCT)
		description = send_c4_command(commands.FIRMWARE_INFO_DESCRIPTION)
		version = send_c4_command(commands.FIRMWARE_INFO_VERSION)

		if(product_info[0] == 1 and description[0] == 1 and version[0] == 1):
			return {'product_info': product_info[1], 'description': description[1], 'version': version[1]}, 200
		else:
			responses = [product_info[1], description[1], version[1]]
			return {'response': ["Couldn't retrieve firmware information", responses]}, 500

class FirmwareInfoProduct(Resource):
    def get(self):
    	serial_return = send_c4_command(commands.FIRMWARE_INFO_PRODUCT)
        return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}

class FirmwareInfoDescription(Resource):
    def get(self):
    	serial_return = send_c4_command(commands.FIRMWARE_INFO_DESCRIPTION)
        return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}

class FirmwareInfoVersion(Resource):
    def get(self):
    	serial_return = send_c4_command(commands.FIRMWARE_INFO_VERSION)
        return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}