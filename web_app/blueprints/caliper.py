from flask import Blueprint, request, render_template, flash

caliper_blueprint = Blueprint('caliper', __name__, url_prefix='/caliper')

TITLE = u"Calibrador de motor"

@caliper_blueprint.route("/")
def index():
	return render_template("caliper/caliper.html", title=TITLE)

@caliper_blueprint.route("/do", methods=["POST"])
def do_caliper():
	if(request.method == "POST"):
		flash(u"Apenas testando a box de outro erro", 'error')
		return render_template("caliper/caliper.html", title=TITLE)

@caliper_blueprint.route("/help")
def help():
	index_helper = u"Aqui deveria ficar o texto explicando como deve funcionar a calibragem"
	return render_template("help.html", title=TITLE, index_helper=index_helper)