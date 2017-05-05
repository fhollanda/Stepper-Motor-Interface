from flask import Blueprint, request, render_template, flash, g, Markup
from forms import Move1DForm
import util.helper as helper
import util.endpoint as endpoint
from util.request_wrapper import post_data

movement_blueprint = Blueprint('movement', __name__, url_prefix='/movement')

TITLE = helper.TITLE['MOVE']
HELP = helper.HELP['MOVE']

@movement_blueprint.before_request
def before_request():
	g.move1d_form = Move1DForm()

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

		steps = form.steps.data
		acquisition_rate = form.acquisition_rate.data

		response = post_data(endpoint.movement + "/{}".format(form.axis_radio.data), data)
		flash('%s |||| %s |||| Dados enviados foram: Eixo="%s", Direcao="%s", Passos=%s, Passos por pontos=%s'  %
		(response, data, form.axis_radio.data, form.direction_radio.data, form.steps.data, form.acquisition_rate.data))

		return render_template("move1d.html", title=TITLE, form=form)

	return render_template("move1d.html", title=TITLE, form=form)

@movement_blueprint.route("/move2d", methods=["GET", "POST"])
def move_2d():
	return render_template("move2d.html", title=TITLE)

@movement_blueprint.route("/move3d", methods=["GET", "POST"])
def move_3d():
	return render_template("move3d.html", title=TITLE)

@movement_blueprint.route("/help")
def help():
	return render_template("help.html", title=TITLE, index_helper=HELP)