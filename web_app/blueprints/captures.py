from flask import Blueprint, request, render_template, flash
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests 
import logging

captures_blueprint = Blueprint('captures', __name__, url_prefix='/captures')

@captures_blueprint.route("/")
def show():
	return render_template("captures.html", captures=get_captures())

def get_captures():
	return requests.get_captures(endpoint.captures)