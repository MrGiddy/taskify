#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from api.v1.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()
    
    return app
