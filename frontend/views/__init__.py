from flask import Blueprint


bp = Blueprint('bp', __name__, url_prefix=None)

from frontend.views.home import *
