from flask import Blueprint, request, render_template, flash
import util.helper as helper
import util.endpoint as endpoint
from util.request_wrapper import get_response

manual_move_blueprint = Blueprint('manual_move', __name__, url_prefix='/manual')

@manual_move_blueprint.route("/")
def show():
	return render_template("manual_move.html")

@manual_move_blueprint.route("/")
def move_to_direction(axis, direction):
	axis = 1
	axis_list = {"x": 4, "y": 3, "z": 1}

	if axis in axis_list:
		data = {	'direction': direction, 'steps': 5, 'acknowledge': True 	}
		response = requests.post_data(endpoint.motor_move + "/{}".format(axis_list.get(axis)), data)

		if(response):
			flash(helper.SCAN_OK.format(scan_name, response.json()['filename']))
		else:
			flash(helper.ERROR['SCAN_EXCEPTION'], helper.FLASH_ERROR)

		return render_template("manual_move.html")