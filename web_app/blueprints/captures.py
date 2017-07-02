from flask import Blueprint, request, render_template, flash, send_file
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests 
import logging, json, StringIO

captures_blueprint = Blueprint('captures', __name__, url_prefix='/captures')

@captures_blueprint.route("/")
def show():
	return render_template("captures.html", captures=get_captures())

@captures_blueprint.route("/<uuid>/<fileformat>")
def get_specific(uuid, fileformat):
	response = requests.get_file(endpoint.capture.format(uuid, fileformat))
	file = response['file']

	if(is_matlab(fileformat)):
		return send_file(get_file_as_stream(file), attachment_filename=uuid+".mat", as_attachment=True)
	else:
		json_file = json.dumps(file, ensure_ascii=False)
		return send_file(get_file_as_stream(json_file), attachment_filename=uuid+".json", as_attachment=True)

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

def is_matlab(string):
	return string.lower() == "matlab"

def get_file_as_stream(value):
	strIO = StringIO.StringIO()
	strIO.write(str(value))
	strIO.seek(0)
	return strIO