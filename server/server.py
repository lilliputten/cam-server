# -*- coding:utf-8 -*-
# @module main
# @since 2019.03.28, 21:32
# @version 2019.03.28, 23:07

#  from config import config
#  from logger import DEBUG

import os

from flask import Flask, url_for, render_template
from flask import request, jsonify
#  import yaml

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


rootPath = os.getcwd()

#  DEBUG('Started')


@app.route('/')
def hello_world():
    #  DEBUG('Get root', {
    #      'version': config['version'],
    #  })
    return '(' + rootPath + ') Index page <a href="' + url_for('hello', name='Some Name') + '">hello</a>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return 'User: %s' % username


@app.route('/upload/<datetag>', methods=['POST'])
def upload(datetag=''):
    app.logger.debug('is_json: ' + str(request.is_json))
    data = request.get_json()
    app.logger.debug('data: ' + str(data))
    image = data['image']
    datetag = data['datetag'] if 'datetag' in data else ''  # None
    app.logger.debug('image: ' + image)
    app.logger.debug('datetag: ' + datetag)
    return jsonify(status='Upload comes here')


@app.route('/uploadJson/', methods=['POST'])
def uploadJson(datetag=''):
    app.logger.debug('is_json: ' + str(request.is_json))
    data = request.get_json()
    app.logger.debug('uploadJson data: ' + str(data))
    image = data['image']
    datetag = data['datetag'] if 'datetag' in data else ''  # None
    app.logger.debug('uploadJson image: ' + image)
    app.logger.debug('uploadJson datetag: ' + datetag)
    return jsonify(status='Upload comes here')


if __name__ == '__main__':
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()
