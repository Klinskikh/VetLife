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
    return render_template('login.html',
                           title='Sign In',
                           form=form)
