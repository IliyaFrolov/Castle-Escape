from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User

class Input(FlaskForm):
    player_input = StringField(validators=[DataRequired()])
    enter = SubmitField('Enter')

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember_me = BooleanField()
    submit = SubmitField()

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
        )
    submit = SubmitField()

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Username already taken")
    
