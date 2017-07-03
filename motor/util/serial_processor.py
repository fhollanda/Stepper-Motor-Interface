import io
import time
import serial
import logging
import commands
from flask_restful import abort

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

		self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

	def close_serial(self):
		time.sleep(0.01)
		if(self.ser.is_open):
			self.ser.close()

	def write_serial(self, writable, delay):
		if delay:
			time.sleep(0.5)
		writable_bytes = writable.encode('ascii')
		self.sio.write(unicode(writable_bytes))

	def read_serial(self):
		self.sio.flush()
		return self.sio.readline()

def send_c4_command(command, delay = False):
	writable = "!" + C4_ID + command + commands.CR
	return send_to_c4(writable, delay)

def send_single_command(command):
	return send_to_c4(command, False)

def send_to_c4(writable, delay):
	try:
		C4SerialProcessor().write_serial(writable, delay)
		serial_line = C4SerialProcessor().read_serial()
		#C4SerialProcessor().close_serial()
	except serial.SerialException as se:
		log_and_abort(503, writable, se)
	except serial.SerialTimeoutException as ste:
		log_and_abort(504, writable, ste)
	except Exception as e:
		log_and_abort(500, writable, e)

	return serial_line or "a"

def log_and_abort(status, data, exception):
	logging.exception("error: " + str(exception))
	abort(status, cause=str(exception), error=str("Couldn't write: " + data))