from flask import Blueprint

views: Blueprint = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
	return 'Welcome Home'

