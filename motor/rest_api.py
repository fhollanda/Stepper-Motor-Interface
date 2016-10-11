from flask import Flask, request, abort
from flask_restful import Api
from flask_cors import CORS
from resources.move_motor import MoveMotor, MoveMotorList, RequestMotorPosition
from resources.copyright_notice import CheckCopyright
from resources.abort_motion import AbortMotion
from resources.home_motor import HomeMotor, HomeMotorList, AbortHomeCommand
from resources.firmware_information import FirmwareInformation

app = Flask("motor")
CORS(app)

@app.before_request
def only_json():
    if request.data and not request.is_json: 
        abort(400)

api = Api(app)

#COPYRIGHT
api.add_resource(CheckCopyright, '/motor/api/copyright')

#ABORT
api.add_resource(AbortMotion, '/motor/api/abort')

#FIRMWARE 
api.add_resource(FirmwareInformation, '/motor/api/firmware')

#HOME
api.add_resource(HomeMotor, '/motor/api/home/go/<int:id>')
api.add_resource(HomeMotorList, '/motor/api/home/go')
api.add_resource(AbortHomeCommand, '/motor/api/home/abort')

#MOVE
api.add_resource(MoveMotor, '/motor/api/move/<int:id>')
api.add_resource(MoveMotorList, '/motor/api/move')
api.add_resource(RequestMotorPosition, '/motor/api/move/position')

if __name__ == '__main__':
	app.run(debug=True)