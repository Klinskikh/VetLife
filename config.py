import os
import yaml

basedir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(basedir, 'config.yaml'), 'r') as f:
    config = yaml.load(f)

WTF_CSRF_ENABLED = True
SECRET_KEY = config['secret_key']

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = '{db_provider}://{db_login}:{db_psw}@{db_ip}/{db_name}'.format(**config)
SQLALCHEMY_TRACK_MODIFICATIONS = True
WHOOSH_BASE = os.path.join(basedir, 'search.db')

service_config = {
    "google": {
        'code': "",
        'url_token': "https://accounts.google.com/o/oauth2/token",
        'url': 'https://accounts.google.com/o/oauth2/auth',
        'url_user_info': "https://www.googleapis.com/oauth2/v2/userinfo",
        'client_id': "{client_id_google}".format(**config),
        'client_secret': "{client_secret_google}".format(**config),
        # 'redirect_uri': "http://vetlife2.klinskih.com/start_oauth",
        'redirect_uri': "http://127.0.0.1:5000/start_oauth",
        'grant_type': 'authorization_code',
        'scope': "https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile",
        'project_id':"vetlife-test",
        'auth_provider_x509_cert_url': "https://www.googleapis.com/oauth2/v1/certs"
    },
    "yandex": {
        'code': '',
        'url': 'https://oauth.yandex.ru/authorize',
        'url_token': 'https://oauth.yandex.ru/token',
        'url_user_info': 'https://login.yandex.ru/info',
        'grant_type': 'authorization_code',
        'client_id': "{client_id_ya}".format(**config),
        'client_secret': "{client_secret_ya}".format(**config),

    },
    "vkontakte": {
        'code': '',
        'url_token': 'https://oauth.vk.com/access_token',
        'url_user_info': 'https://api.vk.com/method/users.get?fields=uid,first_name,last_name,nickname,screen_name,sex,bdate,city,country,timezone,photo',
        'client_id': '...',
        'client_secret': '...',
        'redirect_uri': "http://..."
    }
}
