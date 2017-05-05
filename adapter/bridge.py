from flask import Flask, request, abort
from flask_restful import Api
from flask_cors import CORS
from resources.copyright import Copyright
from resources.movement import SingleAxisMove, MultipleAxisMove

app = Flask("adapter")
CORS(app)

@app.before_request
def only_json():
    if request.data and not request.is_json: 
        abort(400)

api = Api(app)

#COPYRIGHT
api.add_resource(Copyright, '/adapter/api/copyright')

#MOVEMENT
api.add_resource(SingleAxisMove, '/adapter/api/move/<axis>')
api.add_resource(MultipleAxisMove, '/adapter/api/move')

if __name__ == '__main__':
	app.run(debug=True, port=5001)