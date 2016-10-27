from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.copyright import Copyright

app = Flask("adapter")
CORS(app)

api = Api(app)

#COPYRIGHT
api.add_resource(Copyright, '/adapter/api/copyright')

if __name__ == '__main__':
	app.run(debug=True, port=5001)