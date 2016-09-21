import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tagdemo.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY='pepe2016',
USERNAME='admin',
PASSWORD='default'
WTF_CSRF_ENABLED = True
