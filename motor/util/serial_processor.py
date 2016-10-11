import time
import serial
import commands

SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 9600
C4_ID = "1"

class SerialProcessor:
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

	def write_serial(self, writable):
		writable_bytes = writable.encode('ascii')	
		self.ser.write(writable_bytes)

	def read_serial(self):
		return self.ser.readline()

def send_c4_command(command, pre_parameters = "", post_parameters = ""):
	writable = "!" + C4_ID + command + pre_parameters + commands.CR
	serial_response = []
	
	try:
		ser = SerialProcessor()
		ser.write_serial(writable)
		serial_line = ser.read_serial()
		serial_response = [200, serial_line]

		if(post_parameters):
			ser.write_serial(post_parameters)
			serial_another_line = ser.read_serial()
			serial_response = [200, [serial_line, serial_another_line]]

		#ser.close_serial()
	except serial.SerialException as se:
		serial_response = make_error_response(503, writable, se)
	except serial.SerialTimeoutException as ste:
		serial_response = make_error_response(504, writable, ste)
	except Exception as e:
		serial_response = make_error_response(500, writable, e)

	return serial_response

def send_single_command(command):
	serial_response = []

	try:
		ser = SerialProcessor()
		ser.write_serial(command)
		serial_line = ser.read_serial()
		serial_response = [200, serial_line]
	except Exception as e:
		serial_response = make_error_response(500, command, e)

	return serial_response

def make_error_response(status, data, exception):
	print("error: " + str(exception))
	return [status, ["error: Couldn't write: " + data, "cause: " + str(exception)]]