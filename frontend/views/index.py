from flask import render_template
from frontend.views import bp


@bp.route('/index', methods=['GET'])
def index():
    """Display the index page"""
    return render_template('index.html', title='Welcome')
