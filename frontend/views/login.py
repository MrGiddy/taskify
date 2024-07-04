from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from frontend.views import bp
import requests


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Display the login page or send login data to api"""
    form_data = request.form
    # If the request method is POST
    if request.method == 'POST':
        try:
            # Send POST request to api and process response
            resp = requests.post('http://127.0.0.1:5000/api/v1/login', data=form_data)
            message = resp.json().get('message')
            if message == 'Login successful':
                session['user_logged_in'] = True
                return redirect(url_for('bp.index')), 302
            elif message == 'Login failed':
                return render_template('login.html', title='Login'), 400
        except requests.RequestException as e:
            return render_template('login.html', title='Login'), 500
    else:
        # If the request method is GET
        return render_template('login.html', title='Login'), 200
