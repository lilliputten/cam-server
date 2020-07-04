# -*- coding:utf-8 -*-
# @module server
# @since 2019.03.28, 21:32
# @changed 2020.07.04, 01:47

import os
from os import path
import datetime

from config import config

from app import app
from logger import DEBUG
import errors

UPLOAD_FOLDER = path.join(config['uploadPath'])
ALLOWED_EXTENSIONS = {'aaa'}  # 'png', 'jpg', 'jpeg', 'gif'}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


def uploadImage(file):
    filename = file.filename
    name, ext = path.splitext(filename)
    now = datetime.datetime.now()
    timestamp = now.strftime(config['shortDateFormat'])

    data = {
        'filename': filename,
        'name': name,
        'ext': ext,
        'timestamp': timestamp,
    }

    DEBUG('uploadImage', data)

    if ext not in ALLOWED_EXTENSIONS:
        error = 'Unexpected extension: ' + ext
        DEBUG('uploadImage: error: ' + error, data)
        return {'error': error}

    uploadPath = config['uploadPath']
    try:
        if not os.path.exists(uploadPath):
            os.makedirs(uploadPath)
    except Exception, error:
        DEBUG('uploadImage: error catched', {
            'error': errors.toBlockString(error),
        })
        return {'error': 'Upload file creation error (see server log)'}
    finally:
        file.save(os.path.join(uploadPath, 'image'))


__all__ = [  # Exporting objects...
    'uploadImage',
]
