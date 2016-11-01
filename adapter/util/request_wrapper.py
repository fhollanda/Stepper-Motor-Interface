# encoding: utf-8
import requests

err000 = u"Ocorreu um erro, tente novamente mais tarde (err: x000)"
err001 = u"Ocorreu um erro na conexão. Tente novamente ou verifique o funcionamento do motor (err: x001)"
err002 = u"Há alguma falha no funcionamento do adaptador. Verifique os logs (err: x002)"
err503 = u"O serviço se encontra indisponível, tente novamente mais tarde (err: x503)"

def get_response(endpoint):	
	try:
		response = requests.request("GET", endpoint)
		status_code = response.status_code

		if(status_code == requests.codes.ok):
			json_response_message = response.json()['response']
			return to_json(json_response_message)
		else:
			return show_message_for(status_code), status_code
	except requests.exceptions.RequestException as e:
		return to_json(err001), 500
	except Exception as ex:
		return to_json(err002), 500

def show_message_for(status_code):
	if(status_code == requests.codes.unavailable):
		return to_json(err503)
	else:
		return to_json(err000)

def to_json(msg):
	return { 'message' : msg }