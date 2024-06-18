import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    JSONIFY_PRETTYPRINT_REGULAR = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'taskify.db')
