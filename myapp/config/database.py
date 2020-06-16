"""config database"""
# pylint: disable=unused-import
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
import os
import sys
import string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

db = SQLAlchemy()

class Config():
    """Base Configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self, app):
        """constructor"""

class ProductionConfig(Config):
    """Production Configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database_path'

class DevelopmentConfig(Config):
    """Development Configuration"""
    def __init__(self, app):
        """constructor"""
        super().__init__(self)
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///'+\
            os.path.join(app.instance_path, 'flask.sqlite')

class TestingConfig(Config):
    """Testing Configuration"""
    TESTING = True

def init_app(app):
    """init database"""
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    _class = getattr(sys.modules[__name__],\
        string.capwords(app.config['ENV'])+'Config')
    app.config.from_object(_class(app))
    db.app = app
    db.init_app(app)
