# -*- coding:utf-8 -*-
# @module imageUtils
# @since 2020.09.29, 23:56
# @changed 2020.10.28, 03:31

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

import os
import errno
import traceback

from config import config

from logger import DEBUG


def parseIndexLine(s, full=False):
    try:
        parts = s.split('\t')
        id = parts[0]
        ip = parts[1]
        timestamp = parts[2]
        if full:
            return {'id': id, 'ip': ip, 'timestamp': timestamp}
        return id
    except Exception as e:
        error = str(e)
        eTraceback = str(traceback.format_exc())
        DEBUG('imageUtils:parseIndexLine: error', {
            'error': error,
            's': s,
            'traceback': eTraceback,
        })
        raise Exception('Invalid images index line format: \'%s\' (parser message: %s)' % (s, error))


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


def removeImages(ids):
    """
    Remove specified images
    NOTE: Not fails if some of items or item files not exists
    """
    # TODO: Lock file?
    uploadPath = config['uploadPath']
    # Load index..
    imagesList = loadImagesList(True)
    #  filelist = [ file for file in os.listdir(mydir) if file.endswith('.bak') ]  # TODO: Filter example
    DEBUG('imageUtils:removeImages: start', {
        'ids': ids,
        'imagesList': imagesList,
        'uploadPath': uploadPath,
    })
    # Remove items from images list...
    imagesList = list(filter(lambda item: item['id'] not in ids, imagesList))
    # Save updated index file...
    indexFilePath = os.path.join(uploadPath, config['imagesIndex'])
    DEBUG('imageUtils:removeImages: updated list', {
        'ids': ids,
        'imagesList': imagesList,
        'indexFilePath': indexFilePath,
    })
    with open(indexFilePath, 'wb') as indexFile:
        for item in imagesList:
            indexFile.write(item['id'] + '\t' + item['ip'] + '\t' + item['timestamp'] + '\n')
    # Remove single files...
    for id in ids:
        imageFilePath = os.path.join(uploadPath, id + config['imageExt'])
        yamlFilePath = os.path.join(uploadPath, id + '.yaml')
        DEBUG('imageUtils:removeImages: remove item files', {
            'id': id,
            'imageFilePath': imageFilePath,
            'yamlFilePath': yamlFilePath,
        })
        # Try to dlete files ignoring 'not exist' errors...
        try:
            os.remove(imageFilePath)
            DEBUG('imageUtils:removeImages: deleted', {'imageFilePath': imageFilePath})
        except Exception, e:
            if e.errno == errno.ENOENT:
                DEBUG('imageUtils:removeImages: file not exist', {'imageFilePath': imageFilePath})
            else:
                raise
        try:
            os.remove(yamlFilePath)
            DEBUG('imageUtils:removeImages: deleted', {'yamlFilePath': yamlFilePath})
        except Exception, e:
            if e.errno == errno.ENOENT:
                DEBUG('imageUtils:removeImages: file not exist', {'yamlFilePath': yamlFilePath})
            else:
                raise
    DEBUG('imageUtils:removeImages: done', {
        'ids': ids,
        'imagesList': imagesList,
    })


def removeAllImages():
    """
    Remove all images
    """
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
