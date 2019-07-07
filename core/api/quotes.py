import os
import sys
import json
import random
from flask import Blueprint, request, abort, jsonify, g

# Relative Imports
from . import BP_API
from .. import models
from ..config import QUOTES_DATASET


QUOTES_DATA = json.load(open(QUOTES_DATASET, mode="r", encoding='utf-8'))
_QUOTES_DATA_MAX_LEN = len(QUOTES_DATA)

def key_missing_checker(data, keys):
    _schema = {"status": "ok", "message": "ok", "data": None}
    for k in keys:
        if k not in data.keys():
            _schema = {**_schema, **{"status": "error", "message": "required field '{0}' is missing.".format(k)}}
            continue
        if data[k] is None or data[k] == "":
            _schema = {**_schema, **{"status": "error", "message": "required field '{0}' cannot be 'None'.".format(k)}}
    return _schema

@BP_API.route('/quote', methods=['GET'])
def quote():
    """ Base Class to Show random quote """
    _schema = {"random": True}
    _bind = {**_schema, **request.args}
    _kc = key_missing_checker(_bind, ["random"])
    if _kc["status"] == "error":
        return jsonify(_kc)
    if _bind["random"] is True:
        _kc["data"] = QUOTES_DATA[random.randint(0, _QUOTES_DATA_MAX_LEN)]
        return jsonify(_kc)
    return jsonify(_kc)
