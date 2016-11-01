import time
import serial
import commands
from flask import jsonify

SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 9600
C4_ID = "1"

class C4SerialProcessor:
	def __init__(self):
		self.ser = serial.Serial(
			port= SERIAL_PORT, 
			baudrate = SERIAL_BAUDRATE, 
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			timeout=1
		)

	def close_serial(self):
		time.sleep(0.01)
		self.ser.close()

	def write_serial(self, writable, delay):
		if delay:
			time.sleep(0.5)
		writable_bytes = writable.encode('ascii')	
		self.ser.write(writable_bytes)

	def read_serial(self):
		return self.ser.readline()

def send_c4_command(command, delay = True):
	writable = "!" + C4_ID + command + commands.CR
	return send_to_c4(writable, delay)

def send_single_command(command):
	return send_to_c4(command, False)

def send_to_c4(writable, delay):
	serial_response = []

	try:
		ser = C4SerialProcessor()
		ser.write_serial(writable, delay)
		serial_line = ser.read_serial()
		serial_response = [200, serial_line]
		#ser.close_serial()
	except serial.SerialException as se:
		serial_response = make_error_response(503, writable, se)
	except serial.SerialTimeoutException as ste:
		serial_response = make_error_response(504, writable, ste)
	except Exception as e:
		serial_response = make_error_response(500, writable, e)

	return serial_response

def make_error_response(status, data, exception):
	print("error: " + str(exception))
	json_response = {"error": str("Couldn't write: " + data), "cause": str(exception)}
	return [status, json_response]