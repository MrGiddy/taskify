from flask import Blueprint


bp = Blueprint('bp', __name__, url_prefix=None)

from frontend.views.index import *
from frontend.views.about import *
from frontend.views.contact import *
from frontend.views.login import *
from frontend.views.signup import *
from frontend.views.logout import *
from frontend.views.home import *
