from flask import Blueprint

BP_API = Blueprint('api', __name__)

# Relative Imports
from . import quotes
from . import users
