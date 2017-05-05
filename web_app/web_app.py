from flask import Flask
from flask_bootstrap import Bootstrap
from blueprints.caliper import caliper_blueprint
from blueprints.copyright import copyright_blueprint
from blueprints.movement import movement_blueprint
import util.helper as helper

app = Flask("web_app")
app.config.from_object('config')

Bootstrap(app)

app.register_blueprint(caliper_blueprint)
app.register_blueprint(copyright_blueprint)
app.register_blueprint(movement_blueprint)

@app.context_processor
def inject_menu():
    return dict(menu=helper.MENU)

if __name__ == '__main__':
	app.run(debug=True, port=5002),
	use_reloader=True