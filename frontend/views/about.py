from flask import render_template, url_for
from frontend.views import bp


@bp.route('/about', methods=['GET'])
def about():
    """Display the about page"""
    return render_template('about.html', title='About')
