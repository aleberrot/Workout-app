from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
	username: str = StringField('Username', validators=[DataRequired(), Length(min=4)])
	email: str = StringField('Email', validators=[DataRequired(), Length(min=4)])
	password: str = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
	password2: str = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	username: str = StringField('Username', validators=[DataRequired()])
	password: str = PasswordField('Password', validators=[DataRequired()])
	remember_me: bool = BooleanField('Remember me')
	submit: str = SubmitField('Log In')

class WorkoutForm(FlaskForm):
	workout_name: str = StringField('Name of the workout', validators=[DataRequired(), Length(min=10)])
	workout_description: str = TextAreaField('Describe your workout')
	# implement something for the amount of excecises of the workout and the ammount of sets and reps
	submit  = SubmitField('Create Note')
