from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.copyright import Copyright

app = Flask("motor")
CORS(app)

# @app.before_request
# def only_json():
#     if request.data and not request.is_json: 
#         abort(400)

api = Api(app)

#COPYRIGHT
api.add_resource(Copyright, '/adapter/api/copyright')

if __name__ == '__main__':
	app.run(debug=True, port=5001)