from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import os
from config import basedir

FLASK_DEBUG = 1
logger = logging.getLogger('root')
fileHandler = logging.FileHandler(os.path.join(basedir, 'vet_life.log'))
logger.setLevel(logging.INFO)
logger.addHandler(fileHandler)
logger.info(u'Start...')
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
import os
from flask_login import LoginManager
from flask_openid import OpenID



lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from VetLife import views, models


