from flask import Blueprint, request, render_template, flash
import requests
import util.helper as helper
import util.endpoints as endpoint

copyright_blueprint = Blueprint('copyright', __name__, url_prefix='/copyright')

TITLE = helper.TITLE['COPYRIGHT']

@copyright_blueprint.route("/")
def show():
	return render_template("copyright.html", title=TITLE, copyright=get_copyright())

def get_copyright():
	response = requests.request("GET", endpoint.get_copyright)
	return response.json()['message']