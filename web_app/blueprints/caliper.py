from flask import Blueprint, request, render_template, flash, g
from forms import CaliperForm
import util.helper as helper

caliper_blueprint = Blueprint('caliper', __name__, url_prefix='/caliper')

TITLE = helper.TITLE['CALIPER']
HELP = helper.HELP['CALIPER']

@caliper_blueprint.before_request
def before_request():
	g.caliper_form = CaliperForm()

@caliper_blueprint.route("/", methods=["GET", "POST"])
def caliper():
	form = g.get("caliper_form")

	if form.validate_on_submit():
		flash('Os dados enviados foram: Motor="%s", Inicial=%s, Final=%s' %
			(form.motor.data, form.initial_position.data, form.final_position.data))
		return render_template("caliper.html", title=TITLE, form=form)

	return render_template("caliper.html", title=TITLE, form=form)

@caliper_blueprint.route("/test", methods=["POST"])
def test_caliper():
	form = g.get("caliper_form")

	if(request.method == "POST"):
		flash(helper.RANDOM_ERROR, helper.FLASH_ERROR)
		return render_template("caliper.html", title=TITLE, form=form) 

@caliper_blueprint.route("/help")
def help():
	return render_template("help.html", title=TITLE, index_helper=HELP)