import os

class Config(object):
    SECRETE_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'