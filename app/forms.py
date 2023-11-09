from flask_wtf import FlaskForm
from wtf import StringField, TextAreaField, BooleanField, PasswordField, SubmitField
from wtf.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
	username: str = StringField('Username', validators=[DataRequired(), Length(min=4)])
	email: str = StringField('Username', validators=[DataRequired(), Length(min=4)])
	password: str = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
	password2: str = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	username: str = StringField('Username', validators=[DataRequired()])
	password: str = PasswordField('Password', validators=[DataRequired()])
	remember_me: bool = BooleanField('Remember me')
	submit: str = SubmitField('Log In')
