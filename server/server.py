# -*- coding:utf-8 -*-
# @module main
# @since 2019.03.28, 21:32
# @version 2019.03.28, 23:07

from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Index page <a href="' + url_for('hello', name='Some Name') + '">hello</a>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return 'User: %s' % username


if __name__ == '__main__':
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()
