from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField
from wtforms.validators import DataRequired
import util.helper as helper

class CaliperForm(FlaskForm):
	motor = IntegerField('motor', validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])])
	initial_position = IntegerField('initial_position')
	final_position = IntegerField('final_position')

class Move1DForm(FlaskForm):
	steps = IntegerField('steps', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])])

	acquisition_rate = IntegerField('acquisition_rate', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		default=10)

	axis_radio = RadioField(
		'axis_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('x', 'Eixo x'), ('y', 'Eixo y'), ('z', 'Eixo z')], default='x')

	direction_radio = RadioField(
		'direction_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('f', 'Para frente'), ('r', 'Para tras')], default='f')