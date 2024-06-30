from flask import render_template, url_for
from frontend.views import bp


@bp.route('/home', methods=['GET'])
def home():
    """Display the home page"""
    return render_template('home.html', title='Home')
