# -*- coding:utf-8 -*-
# @module listImages
# @since 2020.09.29, 22:02
# @changed 2020.10.04, 01:55

#  from app import app

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

from os import path
import yaml
#  import datetime

from flask import make_response
from flask import send_file
from flask import render_template
#  from flask import url_for
#  from flask import jsonify
#  from flask import request

from config import config

from logger import DEBUG

import imageUtils


def listAllImages():
    list = imageUtils.loadImagesList(True)
    DEBUG('listAllImages called', {
        'list': list,
    })
    if not list or not len(list):
        return render_template('noImages.html')
    return render_template('listAllImages.html', list=list)


def viewImage(id):
    #  return render_template('viewImage.html', id=id)
    uploadPath = config['uploadPath']
    yamlFilePath = path.join(uploadPath, id + '.yaml')
    if not path.isfile(yamlFilePath):
        #  return 'imageNotFound'
        return render_template('imageNotFound.html', id=id)
    with open(yamlFilePath) as yamlFilePathFile:
        params = yaml.load(yamlFilePathFile, Loader=yaml.FullLoader)
        timestamp = params['timestamp']
        imageWidth = config['imageWidth']
        imageHeight = config['imageHeight']
        DEBUG('viewImage called', {
            'yamlFilePath': yamlFilePath,
            'params': params,
        })
        # params data sample:
        # - ext: jpg
        # - filename: test-image.jpg
        # - id: 200930-225108
        # - mimeType: image/jpeg
        # - name: test-image
        # - timestamp: 2020.09.30-22:51:08
        return render_template('viewImage.html', id=id, timestamp=timestamp, imageWidth=imageWidth, imageHeight=imageHeight, params=params)


def viewLastImage():
    id = imageUtils.getLastImageId()
    if not id:
        return render_template('noImages.html')
    #  return viewImage(id)
    resp = make_response(viewImage(id))
    resp.headers.set('Refresh', '30; url=/last')
    return resp


def sendImageFile(id):
    #  return render_template('viewImage.html', id=id)
    uploadPath = config['uploadPath']
    if id == 'last':
        id = imageUtils.getLastImageId()
    imageFilePath = path.join(uploadPath, id + config['imageExt'])
    yamlFilePath = path.join(uploadPath, id + '.yaml')
    if not path.isfile(imageFilePath) or not path.isfile(yamlFilePath):
        #  return 'imageNotFound'
        return render_template('imageNotFound.html', id=id)
    with open(yamlFilePath) as yamlFilePathFile:
        params = yaml.load(yamlFilePathFile, Loader=yaml.FullLoader)
        mimeType = params['mimeType']
        DEBUG('viewImage called', {
            'imageFilePath': imageFilePath,
            'yamlFilePath': yamlFilePath,
            'params': params,
        })
        # params data sample:
        # - ext: jpg
        # - filename: test-image.jpg
        # - id: 200930-225108
        # - mimeType: image/jpeg
        # - name: test-image
        # - timestamp: 2020.09.30-22:51:08
        return send_file(imageFilePath, mimetype=mimeType)
        #  return render_template('viewImage.html', id=id, timestamp=timestamp, imageWidth=imageWidth, imageHeight=imageHeight, params=params)


__all__ = [  # Exporting objects...
    'listAllImages',
    'viewImage',
    'viewLastImage',
    'sendImageFile',
]

if __name__ == '__main__':
    #  listAllImages()
    result = viewImage('200930-225108')
    DEBUG('test listImages', {'result': result})
