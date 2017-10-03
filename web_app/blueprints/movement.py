from flask import Blueprint, request, render_template, flash, g, Markup
from forms import Move1DForm, Move2DForm, ScopeConfigForm
import util.helper as helper
import util.endpoint as endpoint
import util.request_wrapper as requests

movement_blueprint = Blueprint('movement', __name__, url_prefix='/movement')

@movement_blueprint.before_request
def before_request():
	g.scopeconfig_form = ScopeConfigForm()
	g.move1d_form = Move1DForm()
	g.move2d_form = Move2DForm()

@movement_blueprint.route("/", methods=["GET"])
def index():
	return render_template("movement.html")

@movement_blueprint.route("/move1d", methods=["GET", "POST"])
def move_1d():
	config_form = g.get("scopeconfig_form")
	scan_form = g.get("move1d_form")

	if scan_form.move1d.data and scan_form.validate_on_submit():
		scan_name = "Unnamed"
		if(scan_form.name.data):
			scan_name = scan_form.name.data

		data = { 
			'name': scan_name,
			'direction': scan_form.direction_radio.data, 
			'steps':  scan_form.steps.data, 
			'acquisition_rate': scan_form.acquisition_rate.data
		}

		response = requests.post_data(endpoint.movement + "/{}".format(scan_form.axis_radio.data), data)

		if(response):
			flash(helper.SCAN_OK.format(scan_name, response.json()['filename']))
		else:
			flash(helper.ERROR['SCAN_EXCEPTION'], helper.FLASH_ERROR)
	
	elif config_form.set_config.data and config_form.validate_on_submit():
		data = wrap_configs(config_form)

		response = requests.post_data(endpoint.set_scope_config, data)

		if(response):
			flash(helper.SET_CONFIG_OK)
		else:
			flash(helper.ERROR['SET_CONFIG_EXCEPTION'], helper.FLASH_ERROR)

	return render_template("move1d.html", scan_form=scan_form, config_form=config_form)

@movement_blueprint.route("/move2d", methods=["GET", "POST"])
def move_2d():
	config_form = g.get("scopeconfig_form")
	scan_form = g.get("move2d_form")

	if scan_form.move2d.data and scan_form.validate_on_submit():
		scan_name = "Unnamed"
		if(scan_form.name.data):
			scan_name = scan_form.name.data

		if scan_form.axis_secondary_radio.data in scan_form.axis_radio.data:
			flash(helper.ERROR['SAME_AXIS'], helper.FLASH_ERROR)
		else:
			data = {
				'name': scan_name,
				'primary_axis': scan_form.axis_radio.data,
				'direction': scan_form.direction_radio.data, 
				'steps':  scan_form.steps.data, 
				'acquisition_rate': scan_form.acquisition_rate.data,
				'secondary_axis': scan_form.axis_secondary_radio.data,
				'acquisition_offset_rate': scan_form.acquisition_offset_rate.data,
				'secondary_axis_step_size': scan_form.secondary_axis_step_size.data
			}

			response = requests.post_data(endpoint.movement, data)

			if(response):
				flash(helper.SCAN_OK.format(scan_name, response.json()['filename']))
			else:
				flash(helper.ERROR['SCAN_EXCEPTION'], helper.FLASH_ERROR)

	elif config_form.set_config.data and config_form.validate_on_submit():
		data = wrap_configs(config_form)

		response = requests.post_data(endpoint.set_scope_config, data)

		if(response):
			flash(helper.SET_CONFIG_OK)
		else:
			flash(helper.ERROR['SET_CONFIG_EXCEPTION'], helper.FLASH_ERROR)

	return render_template("move2d.html", scan_form=scan_form, config_form=config_form)

@movement_blueprint.route("/move3d", methods=["GET", "POST"])
def move_3d():
	return render_template("move3d.html")

@movement_blueprint.route("/help")
def help():
	return render_template("help.html", subtitle=helper.TITLE['MOVE'], index_helper=helper.HELP['MOVE'])

def wrap_configs(form):
	return { 
		'channel': form.channel.data,
		'frequency': form.frequency.data,
		'cycles': form.cycles.data,
		'averaging': form.averaging.data,
		'v_scale': float(form.v_scale.data),
		't_scale': float(form.t_scale.data) 
	}