# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user
from VetLife.forms import LoginForm
from VetLife.models import User, ROLE_USER, ROLE_ADMIN
from VetLife import oid, app, db, lm
from datetime import datetime
from ..config import service_config
import requests


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    context = dict(title='Sign In',
                   form=form,
                   providers=app.config['OPENID_PROVIDERS'],
                   service_config=service_config)
    return render_template('login.html', **context)


def getInfoGoogle(param_token, param_info):
    param = {}
    param['nickname'] = param_info['id']
    param['email'] = param_info['email']
    param['provider'] = 'google'
    param['dop_info'] = param_info
    return param


def getInfoYandex(param_token, param_info):
    param = {}
    param['user_id'] = param_info['id']
    param['email'] = param_info['default_email']
    param['provider'] = 'yandex'
    param['dop_info'] = param_info
    return param


getInfo = {
    'google': getInfoGoogle,
    'yandex': getInfoYandex
}


@app.route('/start_oauth', methods=['GET', 'POST'])
def start_oauth():
    params = request.values
    if not params['state'] in service_config:
        return u'Параметры не заданы'

    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    service_config[params['state']]['code'] = params['code']
    result = requests.post(service_config[params['state']]['url_token'], data=service_config[params['state']],
                           headers=headers)

    # if 'error' in result.text:
    #     return u'Параметры приложения заданы неверно'

    param_token = result.json()
    user_id = param_token.get('user_id', '')
    get_params = dict(access_token=param_token['access_token'],
                      user_ids=user_id,
                      format='json',
                      oauth_token=param_token['access_token'])
    result = requests.get(service_config[params['state']]['url_user_info'],
                          params=get_params)
    return result.json()
    # output = getInfo[params['state']](param_token, result.json())
    # return output


# @oid.after_login
# def after_login(resp):
#     if resp.email is None or resp.email == "":
#         flash('Invalid login. Please try again.')
#         return redirect(url_for('login'))
#     user = User.query.filter_by(email=resp.email).first()
#     if user is None:
#         nickname = resp.nickname
#         if nickname is None or nickname == "":
#             nickname = resp.email.split('@')[0]
#         user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
#         db.session.add(user)
#         db.session.commit()
#     remember_me = False
#     if 'remember_me' in session:
#         remember_me = session['remember_me']
#         session.pop('remember_me', None)
#     login_user(user, remember=remember_me)
#     return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
