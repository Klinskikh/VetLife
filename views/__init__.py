# -*- coding: utf-8 -*-
from VetLife import app


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Привет мир!'


if __name__ == '__main__':
    app.run()
