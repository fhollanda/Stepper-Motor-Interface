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

def send_and_receive_data(command, pre_parameters = "", post_parameters = ""):
	serialResponse = []
	writable = "!" + C4_ID + command + pre_parameters + commands.CR
	
	try:
		ser = SerialProcessor()
		ser.write_serial(writable)
		serialLine = ser.read_serial()
		serialResponse = [1, serialLine]

		if(post_parameters):
			ser.write_serial(post_parameters)
			serialAnotherLine = ser.read_serial()
			serialResponse = [1, [serialLine, serialAnotherLine]]

		#ser.close_serial()
	except Exception as e:
		print("error: " + str(e))
		serialResponse = [0, ["error: Couldn't write: " + writable, "cause: " + str(e)]]

	return serialResponse