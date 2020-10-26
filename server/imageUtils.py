# -*- coding:utf-8 -*-
# @module imageUtils
# @since 2020.09.29, 23:56
# @changed 2020.10.17, 02:49

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

import os

from config import config

from logger import DEBUG


def parseIndexLine(s, full=False):
    try:
        parts = s.split(' ')
        id = parts[0]
        ip = parts[1]
        timestamp = parts[2]
        if full:
            return {'id': id, 'ip': ip, 'timestamp': timestamp}
        return id
    except Exception as e:
        DEBUG('imageUtils:parseIndexLine: error', {'error': str(e), 's': s})
        raise e


def loadImagesList(full=False):
    uploadPath = config['uploadPath']
    indexFilePath = os.path.join(uploadPath, config['imagesIndex'])
    if os.path.isfile(indexFilePath):
        with open(indexFilePath) as indexFile:
            data = map(lambda s: s.strip(), indexFile.readlines())
            data = map(lambda s: parseIndexLine(s, full), data)
            return list(reversed(data))


def getImageData(id):
    list = loadImagesList(True)
    # TODO: Check for last image exists?
    if list:
        return list[0]


def getLastImageData():
    list = loadImagesList(True)
    # TODO: Check for last image exists?
    if list:
        return list[0]


def getLastImageId():
    data = getLastImageData()
    # TODO: Check for data content?
    if data:
        return data['id']
    #  list = loadImagesList()
    #  if list:
    #      return list[0]


# Aliases (last => recent)...


def getRecentImageData():
    return getLastImageData()


def getRecentImageId():
    return getLastImageId()


def removeAllImages():
    uploadPath = config['uploadPath']
    #  filelist = [ file for file in os.listdir(mydir) if file.endswith('.bak') ]  # TODO: Filter example
    DEBUG('imageUtils:removeAllImages', {'uploadPath': uploadPath})
    for file in os.listdir(uploadPath):
        DEBUG('imageUtils:removeAllImages: remove file', {'file': file})
        os.remove(os.path.join(uploadPath, file))


# TODO: def removeImage(id)


__all__ = [  # Exporting objects...
    'loadImagesList',
    'getImageData',
    'getLastImageId',
    'getLastImageData',
    'getRecentImageId',
    'getRecentImageData',
    'removeAllImages',
]

if __name__ == '__main__':
    list = loadImagesList(True)
    DEBUG('imageUtils test', {
        'list': list,
    })
