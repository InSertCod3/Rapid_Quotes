import os
import sys
from flask import Blueprint, request, abort, jsonify, g

# Relative Imports
from . import BP_API
from .. import models


@BP_API.route('/user', methods=['GET'])
def user():
    """ Base Class to Show info of current user """
    return jsonify({'ERROR': "NOT IMPLEMENTED"})
