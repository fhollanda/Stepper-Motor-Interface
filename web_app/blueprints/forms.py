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
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])], default=100)

	acquisition_rate = IntegerField('acquisition_rate', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])], default=10)

	axis_radio = RadioField(
		'axis_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('x', helper.FIELDS['X']), ('y', helper.FIELDS['Y']), ('z', helper.FIELDS['Z'])], default='x')

	direction_radio = RadioField(
		'direction_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('f', helper.FIELDS['FORWARD']), ('r', helper.FIELDS['REVERSE'])], default='f')

class Move2DForm(FlaskForm):
	steps = IntegerField('steps', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])], default=100)

	acquisition_rate = IntegerField('acquisition_rate', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])], default=10)

	axis_radio = RadioField(
		'axis_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('x', helper.FIELDS['X']), ('y', helper.FIELDS['Y']), ('z', helper.FIELDS['Z'])], default='x')

	direction_radio = RadioField(
		'direction_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('f', helper.FIELDS['FORWARD']), ('r', helper.FIELDS['REVERSE'])], default='f')

	axis_secondary_radio = RadioField(
		'axis_secondary_radio',
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])],
		choices=[('x', helper.FIELDS['X']), ('y', helper.FIELDS['Y']), ('z', helper.FIELDS['Z'])], default='y')

	acquisition_offset_rate = IntegerField('acquisition_offset_rate', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])], default=10)

	secondary_axis_step_size = IntegerField('secondary_axis_step_size', 
		validators=[DataRequired(helper.ERROR['REQUIRED_FIELD'])], default=1)