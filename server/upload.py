# -*- coding:utf-8 -*-
# @module server
# @since 2019.03.28, 21:32
# @changed 2020.07.04, 03:45

import os
from os import path
import datetime
import yaml

from config import config

from app import app
from logger import DEBUG
import errors

UPLOAD_FOLDER = path.join(config['uploadPath'])
mimeTypes = {
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    #  'test': 'image/test',
}
mimeExtensions = mimeTypes.keys()  # {'aaa'}  # 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def uploadImage(file):
    filename = file.filename
    name, extension = path.splitext(filename)
    ext = extension[1:].lower()

    now = datetime.datetime.now()
    timestamp = now.strftime(config['shortDateFormat'])

    data = {
        'filename': filename,
        'name': name,
        'ext': ext,
        'timestamp': timestamp,
    }

    if ext not in mimeExtensions:
        error = 'Unexpected extension (' + ext + ')'
        DEBUG('uploadImage: error: ' + error, data)
        return {'error': error}

    data['mimeType'] = mimeTypes[ext]

    DEBUG('uploadImage: data', data)

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
        imageFilePath = os.path.join(uploadPath, config['imageFile'])
        file.save(imageFilePath)
        yamlFilePath = os.path.join(uploadPath, config['imageYamlFile'])
        yaml.safe_dump(data, open(yamlFilePath, 'w'), encoding='utf-8', allow_unicode=True)
        return {'status': 'success', 'timestamp': timestamp}


__all__ = [  # Exporting objects...
    'uploadImage',
]
