from flask import render_template, url_for
from frontend.views import bp


@bp.route('/contact', methods=['GET'])
def contact():
    """Display the contact page"""
    return render_template('contact.html', title='Contact')
