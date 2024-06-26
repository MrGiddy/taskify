import os

basedir = os.path.abspath(os.path.dirname(__file__))

db_path = os.path.join(basedir, '..', 'taskify.db')

# Ensure the directory for the database exists
if not os.path.exists(os.path.dirname(db_path)):
    os.makedirs(os.path.dirname(db_path))

class Config:
    JSONIFY_PRETTYPRINT_REGULAR = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
