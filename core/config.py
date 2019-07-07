import os
import sys
import json

# Relative Imports
from . import utils

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

QUOTES_DATASET = os.path.join(BASE_DIR, "data", "quotes.json")

class Config(object):
    """[summary]

    Arguments:
        object {[type]} -- [description]
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', None)


class DevelopmentConfig(Config):
    """Development Environment Configuration

    Arguments:
        Config {[type]} -- [description]
    """
    DEBUG = True


class ProductionConfig(Config):
    """Development Production Configuration

    Arguments:
        Config {[type]} -- [description]
    """
    DEBUG = False


class TestingConfig(Config):
    """Development Testing Configuration

    Arguments:
        Config {[type]} -- [description]
    """
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
