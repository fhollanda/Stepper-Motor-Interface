from flask import Blueprint, request, render_template, flash
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests 

captures_blueprint = Blueprint('captures', __name__, url_prefix='/captures')

@captures_blueprint.route("/")
def show():
	return render_template("captures.html", captures_list=get_captures_list())

def get_captures_list():	
	return "ok"