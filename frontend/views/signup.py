from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from frontend.views import bp
import requests


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Display the sigUp page or send signUp data to backend"""
    if request.method == 'POST':
        form_data = request.form
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return render_template('signup.html', title='SignUp'), 400
        try:
            resp = requests.post('http://127.0.0.1:5000/api/v1/signup', data=form_data)
            resp.raise_for_status()
            if resp.ok:
                return redirect(url_for('bp.login')), 302
        except requests.RequestException as e:
            return render_template('signup.html', title='SignUp'), 500
    return render_template('signup.html', title='SignUp'), 200
