from flask import Blueprint, request, render_template, flash
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests 

abort_blueprint = Blueprint('abort', __name__, url_prefix='/abort')

@abort_blueprint.route("/")
def send_abort_signal():
	response = requests.post_data(endpoint.abort)
	return helper.ABORT_OK.format(response.status_code)