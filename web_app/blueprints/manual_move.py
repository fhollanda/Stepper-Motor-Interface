from flask import Blueprint, request, render_template, flash, json
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests

manual_move_blueprint = Blueprint('manual_move', __name__, url_prefix='/manual')

@manual_move_blueprint.route("/")
def show():
	return render_template("manual_move.html")

@manual_move_blueprint.route("/move", methods=["POST"])
def move_to_direction():
	print(request.data)

	data = json.loads(request.data)
	axis = data['axis']
	direction = data['direction']
	data = { 'direction': direction, 'steps': 5	}
	response = requests.post_data(endpoint.move + "/{}".format(axis), data)

	if(response):
		flash(helper.MOVE_OK.format(response.status_code))
	else:
		flash(helper.ERROR['UNFINISHED'], helper.FLASH_ERROR)

	return render_template("manual_move.html")