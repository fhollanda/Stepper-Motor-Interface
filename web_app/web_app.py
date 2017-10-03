#!web_app/env/bin/python
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from blueprints.caliper import caliper_blueprint
from blueprints.copyright import copyright_blueprint
from blueprints.movement import movement_blueprint
from blueprints.captures import captures_blueprint
from blueprints.abort import abort_blueprint
import util.helper as helper
import time, logging

app = Flask("web_app")
app.config.from_object('config')

Bootstrap(app)

app.register_blueprint(caliper_blueprint)
app.register_blueprint(copyright_blueprint)
app.register_blueprint(captures_blueprint)
app.register_blueprint(movement_blueprint)
app.register_blueprint(abort_blueprint)

@app.errorhandler(Exception)
def all_exception_handler(error):
	logging.exception("GenericWebException:")
	return helper.ERROR['EXCEPTION'].format(error), 500

@app.template_filter('strftime')
def _jinja2_filter_datetime(timestamp):
	return time.asctime( time.localtime(timestamp) )

@app.context_processor
def inject_menu():
	return dict(menu=helper.MENU, fields=helper.FIELDS, titles=helper.TITLE, errors=helper.ERROR)

@app.route('/')
def index():
	return render_template('movement.html')

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
	shutdown_server()
	return 'Server shutting down...'

if __name__ == '__main__':
	app.run(debug=True, port=5002, threaded=True),
	use_reloader=True