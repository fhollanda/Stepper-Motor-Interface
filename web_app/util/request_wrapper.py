import requests
import logging
import util.helper as helper

def get_message(endpoint):
	try:
		response = requests.request("GET", endpoint)
		if(response.json()['message']):
			return response.json()['message']
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
		return response
