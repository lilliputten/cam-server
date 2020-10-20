# -*- coding:utf-8 -*-
# @module server
# @since 2019.03.28, 21:32
# @changed 2020.10.21, 00:47

import pathmagic  # noqa

#  import os

#  from flask import current_app as app
from .app import app

from flask import redirect
from flask import render_template
#  from flask import url_for
from flask import jsonify
from flask import request

#  from config import config
#  from .logger import DEBUG

from .upload import uploadImage

import listImages
import removeImages


#  DEBUG('Server started', {
#      'FLASK_ENV': os.getenv('FLASK_ENV'),
#  })


@app.route('/app')
def serveAppFile():
    #  # Method 1: Using `file().read()`
    #  clientTemplatePath = config['clientTemplatePath']
    #  filePath = os.path.join(clientTemplatePath, 'index.html')
    #  return file(filePath).read()
    # Method 2: Using `send_static_file()`
    return app.send_static_file('index.html')


@app.route('/')
def rootPage():
    """
    Default page (last image or all images list)
    """
    return redirect('/last')
    #  return listImages.listAllImages()
    #  return listImages.viewLastImage()


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
    return listImages.viewImage(id)


@app.route('/list')
def listAllImages():
    """
    List images
    """
    return listImages.listAllImages()


@app.route('/last')
def viewLastImage():
    """
    View last image
    """
    return listImages.viewLastImage()


@app.route('/remove')
def removeAllImages():
    """
    Remove all uploaded images
    TODO: Remove image by id
    """
    # TODO: Detect referrer & return back?
    removeImages.removeImages()
    return redirect('/')


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
    ip = request.environ['REMOTE_ADDR']
    file = request.files['file']
    result = uploadImage(ip, file)
    return jsonify(result)


if __name__ == '__main__':
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()
