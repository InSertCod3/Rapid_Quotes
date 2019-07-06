import os
import sys
from flask import Blueprint, request, abort, jsonify, g

# Relative Imports
from . import BP_API
from .. import models


@BP_API.route('/quote', methods=['GET'])
def quote():
    """ Base Class to Show random quote """
    return jsonify({'ERROR': "NOT IMPLEMENTED"})
