# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from VetLife import app
from forms import LoginForm


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Привет мир!'


if __name__ == '__main__':
    app.run()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])