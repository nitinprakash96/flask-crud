from flask_wtf import FlaskForm
from wtforms import PasswordFiels, StringField, SubmitField, ValidationFrild
from wtforms.validators import Datarequired, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
	"""
	Form for new users to create a new account
	"""
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('Username', validators=[DataRequired()])
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[
										DataRequired(),
										EqualTo('confirm_password')
										])


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')
		