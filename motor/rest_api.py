from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.move_motor import MoveMotor
from resources.copyright_notice import CheckCopyright
from resources.abort_motion import AbortMotion

app = Flask("motor")
CORS(app)

api = Api(app)
api.add_resource(MoveMotor, '/motor/api/move')
api.add_resource(CheckCopyright, '/motor/api/copyright')
api.add_resource(AbortMotion, '/motor/api/abort')

if __name__ == '__main__':
	app.run(debug=True)