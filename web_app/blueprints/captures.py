from flask import Blueprint, request, render_template, flash
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests 
import logging

captures_blueprint = Blueprint('captures', __name__, url_prefix='/captures')

@captures_blueprint.route("/")
def show():
	return render_template("captures.html", captures=get_captures())

@captures_blueprint.route("/<uuid>/<fileformat>")
def get_specific(uuid, fileformat):
	flash("Good for you {0} {1}".format(uuid, fileformat))
	return render_template("captures.html", captures=get_captures())

@captures_blueprint.route("/delete/<uuid>")
def delete(uuid):
	is_deleted = requests.delete_capture(endpoint.delete_capture.format(uuid))
	if is_deleted:
		flash(helper.DELETE_CAPTURE_OK.format(uuid))
	else:
		flash(helper.ERROR['DELETE_CAPTURE_EXCEPTION'].format(uuid), helper.FLASH_ERROR)
	return render_template("captures.html", captures=get_captures())

def get_captures():
	return requests.get_captures(endpoint.captures)