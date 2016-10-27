# encoding: utf-8
import requests

err000 = u"Ocorreu um erro, tente novamente mais tarde (err: x000)"
err503 = u"O serviço se encontra indisponível, tente novamente mais tarde (err: x503)"

def show_message_for(status_code):
	if(status_code == requests.codes.unavailable):
		return to_json(err503)
	else:
		return to_json(err000)

def to_json(msg):
	return { 'message' : msg }