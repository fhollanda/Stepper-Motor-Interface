from flask import Blueprint, request, render_template, flash
from forms import CaliperForm
import util.helper as helper

caliper_blueprint = Blueprint('caliper', __name__, url_prefix='/caliper')

TITLE = helper.TITLE['CALIPER']
HELP = helper.HELP['CALIPER']

@caliper_blueprint.route("/")
def form():
	form = CaliperForm()
	return render_template("caliper.html", title=TITLE, form=form)

@caliper_blueprint.route("/do", methods=["POST"])
def do_caliper():
	if(request.method == "POST"):
		flash(helper.RANDOM_ERROR, helper.FLASH_ERROR)
		return form()

@caliper_blueprint.route("/help")
def help():
	return render_template("help.html", title=TITLE, index_helper=HELP)