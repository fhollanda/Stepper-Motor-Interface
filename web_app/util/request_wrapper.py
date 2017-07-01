import requests
import logging
import json
import util.helper as helper
from flask import flash

def get_message(endpoint):
	return get_element(endpoint, "message")

def get_captures(endpoint):
	return get_element(endpoint, "captures")

def get_element(endpoint, element):
	try:
		response = requests.request("GET", endpoint)
		if(response.json()[element]):
			return response.json()[element]
	except requests.exceptions.RequestException as e:
		return helper.ERROR['REQUEST_EXCEPTION'].format(str(e))

def post_data(endpoint, payload = None):
	try:
		response = requests.request("POST", endpoint, json=payload)
		if(response.status_code == requests.codes.ok):
			return response
		else:
			response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		logging.error(e)
		if(response.json()['message']):
			cause = response.json()['message']
			logging.error("last error cause: " + cause)
			flash(unicode(cause), helper.FLASH_ERROR)
		else:
			raise