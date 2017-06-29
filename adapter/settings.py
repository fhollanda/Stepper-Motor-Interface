def init():
	global _isRunning
	_isRunning = False

def start_run():
	global _isRunning
	_isRunning = True

def end_run():
	global _isRunning
	_isRunning = False

def isRunning():
	return _isRunning