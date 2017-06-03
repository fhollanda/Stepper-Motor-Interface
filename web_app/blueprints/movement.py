from flask import Blueprint, request, render_template, flash, g, Markup, send_file
from forms import Move1DForm, Move2DForm
import util.helper as helper
import util.endpoint as endpoint
from util.request_wrapper import post_data
import StringIO, uuid, json

movement_blueprint = Blueprint('movement', __name__, url_prefix='/movement')

TITLE = helper.TITLE['MOVE']
HELP = helper.HELP['MOVE']

@movement_blueprint.before_request
def before_request():
	g.move1d_form = Move1DForm()
	g.move2d_form = Move2DForm()

@movement_blueprint.route("/", methods=["GET"])
def index():
	return render_template("movement.html", title=TITLE)

@movement_blueprint.route("/move1d", methods=["GET", "POST"])
def move_1d():
	form = g.get("move1d_form")

	if form.validate_on_submit():
		data = { 
			'direction': form.direction_radio.data, 
			'steps':  form.steps.data, 
			'acquisition_rate': form.acquisition_rate.data 
		}

		response = post_data(endpoint.movement + "/{}".format(form.axis_radio.data), data)

		if(response):
			return send_file(create_file(response), attachment_filename=create_name(), as_attachment=True)
		else:
			flash(helper.SCAN_EXCEPTION, helper.FLASH_ERROR)

		return render_template("move1d.html", title=TITLE, form=form)

	return render_template("move1d.html", title=TITLE, form=form)

@movement_blueprint.route("/move2d", methods=["GET", "POST"])
def move_2d():
	form = g.get("move2d_form")

	if form.validate_on_submit():
		data = {
			'primary_axis': form.axis_radio.data,
			'direction': form.direction_radio.data, 
			'steps':  form.steps.data, 
			'acquisition_rate': form.acquisition_rate.data,
			'secondary_axis': form.axis_secondary_radio.data,
			'acquisition_offset_rate': form.acquisition_offset_rate.data,
			'secondary_axis_step_size': form.secondary_axis_step_size.data
		}

		response = post_data(endpoint.movement, data)

		if(response):
			return send_file(create_file(response), attachment_filename=create_name(), as_attachment=True)
		else:
			flash(helper.SCAN_EXCEPTION, helper.FLASH_ERROR)

		return render_template("move2d.html", title=TITLE, form=form)

	return render_template("move2d.html", title=TITLE, form=form)

@movement_blueprint.route("/move3d", methods=["GET", "POST"])
def move_3d():
	return render_template("move3d.html", title=TITLE)

@movement_blueprint.route("/help")
def help():
	return render_template("help.html", title=TITLE, index_helper=HELP)

def create_file(response):
	strIO = StringIO.StringIO()
	returnable = json.dumps(response)
	strIO.write(str(returnable))
	strIO.seek(0)
	return strIO

def create_name():
	random = uuid.uuid4()
	random.fields[5]
	return "data_" + str(random) + ".json"