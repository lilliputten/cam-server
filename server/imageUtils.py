# -*- coding:utf-8 -*-
# @module imageUtils
# @since 2020.09.29, 23:56
# @changed 2020.10.01, 00:41

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

import os

from config import config

from logger import DEBUG


def parseIndexLine(s, full=False):
    parts = s.split(' ', 1)
    id = parts[0]
    timestamp = parts[1]
    if full:
        return {'id': id, 'timestamp': timestamp}
    return id


def loadImagesList(full=False):
    uploadPath = config['uploadPath']
    indexFilePath = os.path.join(uploadPath, config['imagesIndex'])
    if os.path.isfile(indexFilePath):
        with open(indexFilePath) as indexFile:
            data = map(lambda s: s.strip(), indexFile.readlines())
            data = map(lambda s: parseIndexLine(s, full), data)
            return list(reversed(data))


__all__ = [  # Exporting objects...
    'loadImagesList',
]

if __name__ == '__main__':
    list = loadImagesList(True)
    DEBUG('imageUtils test', {
        'list': list,
    })
