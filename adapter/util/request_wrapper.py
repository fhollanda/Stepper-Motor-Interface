import requests
import logging
import util.helper as helper
from flask_restful import abort
import settings

def post_data(endpoint, payload = None, check_settings = False):
	if(check_settings):
		if(settings._isRunning):
			return post(endpoint, payload)
		else:
			logging.error(helper.ABORT_FLAG)
			abort(500)
	else:
		return post(endpoint, payload)
		
def post(endpoint, payload = None):
	response = wrap_request("POST", endpoint, json=payload)
	return response
	
def get_data(endpoint):	
	response = wrap_request("GET", endpoint)
	return response

def wrap_request(method, endpoint, **kwargs):
	try:
		response = requests.request(method, endpoint, **kwargs)
		if(response.status_code == requests.codes.ok):
			return response
		else:
			response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		logging.error(e)
		return error_response(e.response.status_code, response)
	except requests.exceptions.RequestException as re:
		logging.error(re)
		abort(500, message=helper.ERROR['REQUEST_EXCEPTION'])
	except Exception as ex:
		logging.error(ex)
		abort(500, message=helper.ERROR['GENERIC_REQUEST_EXCEPTION'])

	'''
	This HTTPError exception handling should only be used for translations
	For english version, the 'requests' library already has the text reason 
	See more:
	https://github.com/kennethreitz/requests/blob/master/requests/models.py  
	https://github.com/kennethreitz/requests/blob/master/requests/status_codes.py

	'''
def error_response(status_code, response):
	if(status_code == requests.codes.unavailable):
		abort(status_code, message=helper.ERROR['UNAVAILABLE_SERVICE'])
	elif(status_code == requests.codes.not_found):
		abort(status_code, message=helper.ERROR['NOT_FOUND'])
	elif(status_code == requests.codes.unprocessable_entity):
		abort(status_code, message=helper.ERROR['UNPROCESSABLE_ENTITY'])
	else:
		abort(status_code, message=helper.ERROR['GENERIC_HTTP_ERROR'].format(response))