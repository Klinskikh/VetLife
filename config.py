import os
WTF_CSRF_ENABLED = True
SECRET_KEY = '123'


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


basedir = os.path.abspath(os.path.dirname(__file__))
params = dict(login='kerlaeda_vetlife', psw='p5rNIfl3'
              , db_ip='92.53.123.96', db_name='kerlaeda_vetlife')

SQLALCHEMY_DATABASE_URI = 'mysql://{login}:{psw}@{db_ip}/{db_name}'.format(**params)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
