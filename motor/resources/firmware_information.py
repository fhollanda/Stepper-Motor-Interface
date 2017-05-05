from flask_restful import Resource
from util.serial_processor import send_c4_command
import util.commands as commands


class FirmwareInformation(Resource):
	def get(self):
		product_info = send_c4_command(commands.FIRMWARE_INFO_PRODUCT)
		description = send_c4_command(commands.FIRMWARE_INFO_DESCRIPTION)
		version = send_c4_command(commands.FIRMWARE_INFO_VERSION)

		return {'product_info': product_info, 'description': description, 'version': version}, 200

class FirmwareInfoProduct(Resource):
	def get(self):
		serial_return = send_c4_command(commands.FIRMWARE_INFO_PRODUCT)
		return {'response': serial_return}, 200

class FirmwareInfoDescription(Resource):
	def get(self):
		serial_return = send_c4_command(commands.FIRMWARE_INFO_DESCRIPTION)
		return {'response': serial_return}, 200

class FirmwareInfoVersion(Resource):
	def get(self):
		serial_return = send_c4_command(commands.FIRMWARE_INFO_VERSION)
		return {'response': serial_return}, 200