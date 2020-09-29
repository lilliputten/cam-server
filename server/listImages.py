# -*- coding:utf-8 -*-
# @module listImages
# @since 2020.09.29, 22:02
# @changed 2020.09.29, 23:56

#  from app import app

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

from os import path
import yaml
#  import datetime

from flask import render_template
#  from flask import url_for
#  from flask import jsonify
#  from flask import request

from config import config

from logger import DEBUG
#  import errors

from imageUtils import loadImagesList


def listImages():
    list = loadImagesList()
    DEBUG('listImages called', {
        'list': list,
    })
    if not list or not len(list):
        return render_template('noImages.html')
    return render_template('listImages.html', list=list)


def viewImage(id):
    #  return render_template('viewImage.html', id=id)
    uploadPath = config['uploadPath']
    imageFilePath = path.join(uploadPath, id + config['imageExt'])
    yamlFilePath = path.join(uploadPath, id + '.yaml')
    if not path.isfile(imageFilePath) or not path.isfile(yamlFilePath):
        #  return 'imageNotFound'
        return render_template('imageNotFound.html', id=id)
    params = yaml.load(yamlFilePath, Loader=yaml.FullLoader)
    DEBUG('viewImage called', {
        'params': params,
    })
    return render_template('viewImage.html', id=id, params=params)


__all__ = [  # Exporting objects...
    'listImages',
    'viewImage',
]

if __name__ == '__main__':
    #  listImages()
    result = viewImage('xxx')
    DEBUG('test listImages', {'result': result})
