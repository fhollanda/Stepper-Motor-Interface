import os, uuid, json, logging

def create_path(directory):
	current_path = os.path.dirname(os.path.abspath(__file__))
	parent_path = os.path.dirname(os.path.normpath(current_path))
	return os.path.join(parent_path, directory)

captures_path = create_path("captures/")

def save(data, filepath):
	try:
		logging.warning("create file on {}".format(filepath))
		f = open(filepath, 'w+')
		f.write(json.dumps(data))
		f.close()
	except Exception as e:
		raise

def load(filepath):
	try:
		logging.warning("load file on {}".format(filepath))
		f = open(filepath, 'r')
		data = f.read()
		f.close()
		return data
	except Exception as e:
		raise

def check(filepath):
	try:
		file_exists = os.path.exists(filepath)
		logging.warning("check if file/dir exists: {0}...{1}".format(filepath, file_exists))
		return file_exists
	except Exception as e:
		raise

def delete(filepath):
	try:
		logging.warning("delete file: {}".format(filepath))
		os.remove(filepath)
	except Exception as e:
		raise
		
def create_uuid_filename(fields_quantity = 5):
	random = uuid.uuid4()
	random.fields[fields_quantity]
	return str(random)