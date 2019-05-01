from flask import Blueprint

options = Blueprint('options', __name__)

from . import views
