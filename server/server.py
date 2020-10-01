# -*- coding:utf-8 -*-
# @module server
# @since 2019.03.28, 21:32
# @changed 2020.10.01, 00:41

#  from flask import current_app as app
from .app import app

from flask import render_template
#  from flask import url_for
from flask import jsonify
from flask import request

from config import config

from .logger import DEBUG

from .upload import uploadImage
#  from .listImages import listImages, viewImage
import listImages  # import listImages, viewImage


#  def env_override(value, key):
#    return os.getenv(key, value)
#
#  environment.filters['env_override'] = env_override


@app.route('/')
@app.route('/list')
def rootPage():
    """
    Root page (images list)
    """
    DEBUG('Get root', {
        'version': config['version'],
        'rootPath': config['rootPath'],
    })
    #  rootPath = config['rootPath']
    return listImages.listImages()


@app.route('/image/<id>')
def sendImageFile(id=None):
    """
    Send image file
    """
    return listImages.sendImageFile(id)


@app.route('/view/<id>')
def viewImage(id=None):
    """
    View image
    """
    # TODO: Create image viewer
    return listImages.viewImage(id)


# Tests...


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return 'User: %s' % username


# Upload image...


@app.route('/upload', methods=['POST'])
def upload():
    result = uploadImage(request.files['file'])
    return jsonify(result)


if __name__ == '__main__':
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()
