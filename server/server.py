# -*- coding:utf-8 -*-
# @module server
# @since 2019.03.28, 21:32
# @changed 2020.09.29, 22:02

#  from flask import current_app as app
from .app import app

from flask import render_template
#  from flask import url_for
from flask import jsonify
from flask import request

#  from os import path

from config import config

from .logger import DEBUG

from .upload import uploadImage
from .listImages import listImages


@app.route('/')
def hello_world():
    DEBUG('Get root', {
        'version': config['version'],
        'rootPath': config['rootPath'],
    })
    #  rootPath = config['rootPath']
    return listImages()


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return 'User: %s' % username


@app.route('/upload', methods=['POST'])
def upload():
    result = uploadImage(request.files['file'])
    return jsonify(result)


if __name__ == '__main__':
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()
