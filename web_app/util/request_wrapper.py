import requests
import util.helper as helper

def get_data(endpoint):
	try:
		response = requests.request("GET", endpoint)
		if(response.json()['message']):
			return response.json()['message']
	except requests.exceptions.RequestException as e:
		return helper.ERROR['REQUEST_EXCEPTION'].format(str(e))
	except Exception as ex:
		return helper.ERROR['EXCEPTION'].format(str(ex))

def post_data(endpoint, payload = None):
	try:
		response = requests.request("POST", endpoint, json=payload)
		return response.json()['message']
	except requests.exceptions.RequestException as e:
		return helper.ERROR['REQUEST_EXCEPTION'].format(str(e))
	except Exception as ex:
		return helper.ERROR['EXCEPTION'].format(str(ex))