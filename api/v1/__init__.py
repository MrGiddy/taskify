#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api.config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/v1/*": {"origins": "http://127.0.0.1:5001"}})

    db.init_app(app)

    from api.v1.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()
    
    return app
