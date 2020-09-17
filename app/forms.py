from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class Input(FlaskForm):
    player_input = StringField(validators=[DataRequired()])
    submit = SubmitField()