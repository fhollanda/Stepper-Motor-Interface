from flask import Blueprint, request, render_template, flash
import util.helper as helper

copyright_blueprint = Blueprint('copyright', __name__, url_prefix='/copyright')

TITLE = helper.TITLE['COPYRIGHT']

@copyright_blueprint.route("/")
def show():
	return render_template("copyright.html", title=TITLE, copyright=get_copyright())

def get_copyright():
	return "a resposta deveria estar aqui"