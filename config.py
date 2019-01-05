import os

class Config(object):
    SECRET_KEY="my_secret_key"

class DevelopmentConfig:
    DEBUG=True
    SQLALCHEMY_DATABASE_URL="mysql://root:@localhost/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS=False