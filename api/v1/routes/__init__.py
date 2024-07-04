from flask import Blueprint
from api.v1 import db


bp = Blueprint('bp', __name__, url_prefix='/api/v1')

from api.v1.routes.create import *
from api.v1.routes.retrieve import *
from api.v1.routes.update import *
from api.v1.routes.delete import *
from api.v1.routes.signup import *
from api.v1.routes.login import *
