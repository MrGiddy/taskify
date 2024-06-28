from flask import render_template
from frontend.views import bp


@bp.route('/home', methods=['GET'])
def home():
    """Display all the tasks in the page"""
    return render_template('home.html')
