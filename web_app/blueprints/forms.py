from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CaliperForm(Form):
    motor = IntegerField('motor', validators=[DataRequired()])
    initial_position = IntegerField('initial_position')
    final_position = IntegerField('final_position')