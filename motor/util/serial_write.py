import time
import serial

def do_command(command, parameters = "", acknowledge = False):
	serialResponse = []

	c4Flag = "1"
	acknowledgeFlag = "n" if(acknowledge) else ""

	writable = "!" + c4Flag + command + parameters + acknowledgeFlag + "\r"
	
	writable_bytes = writable.encode('ascii')	

	try:
		ser = serial.Serial(
		                port='/dev/ttyUSB0',
		                baudrate = 9600,
		                parity=serial.PARITY_NONE,
		                stopbits=serial.STOPBITS_ONE,
		                bytesize=serial.EIGHTBITS,
		                timeout=1
		)

		time.sleep(1)	
		ser.write(writable_bytes)
		serialResponse = [1, ser.readline()]
	except Exception as e:
		print("error: " + str(e))
		serialResponse = [0, "Couldn't write: " + writable]

	return serialResponse