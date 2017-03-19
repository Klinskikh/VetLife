# -*- coding: utf-8 -*-
from VetLife import app
from .auth import login


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Привет мир!'


if __name__ == '__main__':
    app.run()
