from flask import Flask
from flask_bootstrap import Bootstrap
from blueprints.caliper import caliper_blueprint
from blueprints.copyright import copyright_blueprint
import util.helper as helper

app = Flask("web_app")
app.secret_key = 'web_app_magic'
Bootstrap(app)

app.register_blueprint(caliper_blueprint)
app.register_blueprint(copyright_blueprint)

@app.context_processor
def inject_menu():
    return dict(menu=helper.MENU)

if __name__ == '__main__':
	app.run(debug=True, port=5002),
	use_reloader=True