import logging

def init():
	global _isRunning
	_isRunning = False

def start_run(resource = None):
	global _isRunning
	_isRunning = True
	if resource: logging.warning(resource + ": start run")

def end_run():
	global _isRunning
	_isRunning = False
	logging.warning("run finished")

def isRunning():
	return _isRunning