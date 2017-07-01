from flask import Flask
from flask_restful import Resource
import dictionaries.capturesdb as db
import json

class CapturesList(Resource):
    def get(self):
        return {'captures': db.get_all_captures()}

class Capture(Resource):
	def __init__(self):
		#colocar campos necessarios para retornar uma captura especifica
		#o id eh o --- hash ---
		#o formato sao primeiramente dois: json e matlab
		pass

	def get(self, id, format):
		#obter elemento especifico
		pass

	def post(self, id):
		#criar um novo elemento
		pass

	def delete(self, id):
		#deletar tanto da lista de itens existentes como tambem o arquivo 
		pass