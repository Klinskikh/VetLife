import os
import yaml
basedir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(basedir,'config.yaml'), 'r') as f:
    config = yaml.load(f)

WTF_CSRF_ENABLED = True
SECRET_KEY = config['secret_key']


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

SQLALCHEMY_DATABASE_URI = '{db_provider}://{db_login}:{db_psw}@{db_ip}/{db_name}'.format(**config)
SQLALCHEMY_TRACK_MODIFICATIONS = True
WHOOSH_BASE = os.path.join(basedir, 'search.db')
