from flask import Flask
from flask_bootstrap import Bootstrap
from blueprints.caliper import caliper_blueprint

app = Flask("web_app")
app.secret_key = 'web_app_magic'
Bootstrap(app)

app.register_blueprint(caliper_blueprint)

if __name__ == '__main__':
	app.run(debug=True),
	use_reloader=True