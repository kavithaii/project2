import os
basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sites.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sites.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
