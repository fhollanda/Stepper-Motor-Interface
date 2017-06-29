from flask import Flask, request, abort
from flask_restful import Api
from flask_cors import CORS
from resources.copyright import Copyright
from resources.movement import SingleAxisMove, DoubleAxisMove
from resources.scope import SetScopeConfig
from resources.abort import Abort
import settings

app = Flask("adapter")
CORS(app)

@app.before_request
def only_json():
    if request.data and not request.is_json: 
        abort(400)

api = Api(app)

#ABORT
api.add_resource(Abort, '/adapter/api/abort')

#COPYRIGHT
api.add_resource(Copyright, '/adapter/api/copyright')

#MOVEMENT
api.add_resource(SingleAxisMove, '/adapter/api/move/<axis>')
api.add_resource(DoubleAxisMove, '/adapter/api/move')

#SCOPE
api.add_resource(SetScopeConfig, '/adapter/api/scope/config')

if __name__ == '__main__':
	settings.init()
	app.run(debug=True, port=5001, threaded=True)