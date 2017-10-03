from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, DecimalField, SubmitField
from wtforms.validators import DataRequired
import util.helper as helper

class CaliperForm(FlaskForm):
	motor = IntegerField('motor', validators=[DataRequired()])
	initial_position = IntegerField('initial_position')
	final_position = IntegerField('final_position')

class ScopeConfigForm(FlaskForm):
	channel = IntegerField('channel')
	frequency = IntegerField('frequency')
	cycles = IntegerField('cycles')
	averaging = IntegerField('averaging')
	v_scale = DecimalField('v_scale')
	t_scale = DecimalField('t_scale')
	set_config = SubmitField(helper.FIELDS['SET_CONFIG_BUTTON'])

class Move1DForm(FlaskForm):
	name = StringField(helper.FIELDS['SCAN_NAME'])

	steps = IntegerField('steps', 
		validators=[DataRequired(helper.FIELDS['STEPS'])], default=100)

	acquisition_rate = IntegerField('acquisition_rate', 
		validators=[DataRequired(helper.FIELDS['ACQUISTION_RATE'])], default=10)

	axis_radio = RadioField(
		'axis_radio',
		validators=[DataRequired(helper.FIELDS['AXIS'])],
		choices=[('x', helper.FIELDS['X']), ('y', helper.FIELDS['Y']), ('z', helper.FIELDS['Z'])], default='x')

	direction_radio = RadioField(
		'direction_radio',
		validators=[DataRequired(helper.FIELDS['DIRECTION'])],
		choices=[('f', helper.FIELDS['FORWARD']), ('r', helper.FIELDS['REVERSE'])], default='f')

	move1d = SubmitField(helper.FIELDS['SCAN_BUTTON'])

class Move2DForm(FlaskForm):
	name = StringField(helper.FIELDS['SCAN_NAME'])
	
	steps = IntegerField('steps', 
		validators=[DataRequired(helper.FIELDS['STEPS'])], default=100)

	acquisition_rate = IntegerField('acquisition_rate', 
		validators=[DataRequired(helper.FIELDS['ACQUISTION_RATE'])], default=10)

	axis_radio = RadioField(
		'axis_radio',
		validators=[DataRequired(helper.FIELDS['AXIS'])],
		choices=[('x', helper.FIELDS['X']), ('y', helper.FIELDS['Y']), ('z', helper.FIELDS['Z'])], default='x')

	direction_radio = RadioField(
		'direction_radio',
		validators=[DataRequired(helper.FIELDS['DIRECTION'])],
		choices=[('f', helper.FIELDS['FORWARD']), ('r', helper.FIELDS['REVERSE'])], default='f')

	axis_secondary_radio = RadioField(
		'axis_secondary_radio',
		validators=[DataRequired(helper.FIELDS['SECONDARY_AXIS'])],
		choices=[('x', helper.FIELDS['X']), ('y', helper.FIELDS['Y']), ('z', helper.FIELDS['Z'])], default='y')

	acquisition_offset_rate = IntegerField('acquisition_offset_rate', 
		validators=[DataRequired(helper.FIELDS['TOTAL_STEPS_SECONDARY'])], default=10)

	secondary_axis_step_size = IntegerField('secondary_axis_step_size', 
		validators=[DataRequired(helper.FIELDS['SIZE_STEPS_SECONDARY'])], default=1)

	move2d = SubmitField(helper.FIELDS['SCAN_BUTTON'])