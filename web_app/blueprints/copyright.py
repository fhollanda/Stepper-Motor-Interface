from flask import Blueprint, request, render_template, flash
import util.helper as helper
import util.endpoint as endpoint
from util.request_wrapper import get_data

copyright_blueprint = Blueprint('copyright', __name__, url_prefix='/copyright')

TITLE = helper.TITLE['COPYRIGHT']

@copyright_blueprint.route("/")
def show():
	return render_template("copyright.html", title=TITLE, copyright=get_copyright())

def get_copyright():	
	return get_data(endpoint.copyright)