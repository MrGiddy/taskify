from flask import render_template, url_for
from frontend.views import bp


@bp.route('/signup', methods=['GET'])
def signup():
    """Display the sigUp page"""
    return render_template('signup.html', title='SignUp')
