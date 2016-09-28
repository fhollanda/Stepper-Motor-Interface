import time
import serial
import commands

SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 9600
C4_ID = 1

def serial_process(command, parameters = "", acknowledge = False):
	serialResponse = []
	acknowledgeFlag = "n" if(acknowledge) else ""
	writable = "!" + C4_ID + command + parameters + acknowledgeFlag + commands.CR
	writable_bytes = writable.encode('ascii')	

	try:
		ser = serial.Serial(
					port= SERIAL_PORT, 
					baudrate = SERIAL_BAUDRATE, 
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