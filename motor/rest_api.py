from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.move_motor import MoveMotor
from resources.copyright_notice import CheckCopyright

app = Flask("motor")
CORS(app)

api = Api(app)
api.add_resource(MoveMotor, '/motor/api/move')
api.add_resource(CheckCopyright, '/motor/api/copyright')

if __name__ == '__main__':
	app.run(debug=True)