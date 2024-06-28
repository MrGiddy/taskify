#!/usr/bin/env python3
from flask import Flask
from frontend.views import bp


app = Flask(__name__)
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
