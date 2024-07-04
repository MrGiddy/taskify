from flask import render_template
from frontend.views import bp

@bp.route('/')
@bp.route('/home')
def home():
    """Display the home page"""
    return render_template('home.html', title='Welcome')
