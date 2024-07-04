from flask import jsonify
from flask import request
from api.v1.routes import bp


@bp.route('/signup', methods=['POST'])
def signup():
    """Process the SignUp form"""
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    return jsonify({'message': 'signup success'}), 200
