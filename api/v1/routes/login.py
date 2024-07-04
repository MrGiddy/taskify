from api.v1.routes import bp
from flask import jsonify
from flask import request


@bp.route('/login', methods=['POST'])
def login():
    """Login a User"""
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'matbin' and password == 'password':
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 400
