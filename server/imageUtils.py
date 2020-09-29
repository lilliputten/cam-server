# -*- coding:utf-8 -*-
# @module listImages
# @since 2020.09.29, 23:56
# @changed 2020.09.29, 23:56

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

import os

from config import config

from logger import DEBUG


def loadImagesList():
    uploadPath = config['uploadPath']
    indexFilePath = os.path.join(uploadPath, config['imagesIndex'])
    if os.path.isfile(indexFilePath):
        with open(indexFilePath) as indexFile:
            return list(reversed(map(lambda s: s.strip(), indexFile.readlines())))


__all__ = [  # Exporting objects...
    'loadImagesList',
]

if __name__ == '__main__':
    list = loadImagesList()
    DEBUG()
