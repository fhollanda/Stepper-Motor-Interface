import shelve, logging, os
from cPickle import HIGHEST_PROTOCOL
import util.filemanager as filemg

CAPTURES_DB = 'captures.db'

def open_db():
	current_path = os.path.dirname(os.path.abspath(__file__))
	filepath = os.path.join(current_path, CAPTURES_DB) 
	return shelve.open(filepath, protocol=HIGHEST_PROTOCOL, writeback=True)

db = open_db()

def save_capture(key, data):
	try:
		db[key] = data
		logging.warning("store capture with " + str(data))
	except Exception as e:
		logging.error(e)

def delete_capture(key):
	try:
		filepath = filemg.captures_path + key
		file_exists = filemg.check(filepath) and db.has_key(key)

		if file_exists:
			filemg.delete(filepath)
			del db[key]
			return True
		else:
			return False
	except Exception as e:
		logging.error(e)
		return False

def get_all_captures():
	try:
		keylist = db.keys()
		dbdict = {}
		
		for key in keylist:
			value = db[key]
			dbdict[key] = value

		return dbdict
	except Exception as e:
		logging.error(e)