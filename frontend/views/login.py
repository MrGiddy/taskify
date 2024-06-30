from flask import render_template, url_for
from frontend.views import bp


@bp.route('/login', methods=['GET'])
def login():
    """Display the login page"""
    return render_template('login.html', title='Login')
