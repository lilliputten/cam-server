# -*- coding:utf-8 -*-
# @module listImages
# @since 2020.09.29, 22:02
# @changed 2020.09.29, 23:25

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

import os
#  from os import path
#  import datetime
#  import yaml

from config import config

from logger import DEBUG
#  import errors


def loadImagesList():
    uploadPath = config['uploadPath']
    indexFilePath = os.path.join(uploadPath, config['imagesIndex'])
    if os.path.isfile(indexFilePath):
        with open(indexFilePath) as indexFile:
            return map(lambda s: s.strip(), indexFile.readlines())


def listImages():
    list = loadImagesList()
    DEBUG('listImages called', {
        'list': list,
    })
    #  return render_template('listImages.html', list=list)
    return 'listImages'


__all__ = [  # Exporting objects...
    'listImages',
]

if __name__ == '__main__':
    listImages()
