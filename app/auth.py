from flask import Blueprint, redirect, url_for, render_template, flash
from .forms import RegisterForm, LoginForm

auth: Blueprint = Blueprint('auth', __name__)

@auth.route('/register')
def register():
	form: RegisterForm = RegisterForm()
	return render_template('register.html', form=form)


@auth.route('/login')
def login():
	form: LoginForm = LoginForm()
	return render_template('login.html', form=form)



@auth.route('/logout')
def logout():
	return 'You are were logged out'


