
from flask import Blueprint

auth = Blueprint('home', __name__)

from . import views