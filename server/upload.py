# -*- coding:utf-8 -*-
# @module server
# @since 2019.03.28, 21:32
# @changed 2020.07.04, 01:47

from .app import app

import os
from os import path

#  from flask import request, jsonify

from .config import config
from .logger import DEBUG

UPLOAD_FOLDER = path.join(config['uploadPath'])
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


def uploadImage(file, datetag=''):
    filename = file.filename
    name, ext = path.splitext(filename)
    DEBUG('uploadImage', {
        'filename': filename,
        'name': name,
        'ext': ext,
        'datetag': datetag,
    })
    uploadPath = config['uploadPath']
    try:
        if not os.path.exists(uploadPath):
            os.makedirs(uploadPath)
    finally:
        file.save(os.path.join(uploadPath, 'image'))
    #  if image and allowed_file(file.filename):
    #      print '**found file', file.filename
    #      filename = secure_filename(file.filename)
    #      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #      # for browser, add 'redirect' function on top of 'url_for'
    #      return url_for('uploaded_file',
    #                              filename=filename)


__all__ = [  # Exporting objects...
    'uploadImage',
]
