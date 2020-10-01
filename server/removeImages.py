# -*- coding:utf-8 -*-
# @module removeImages
# @since 2020.10.01, 23:40
# @changed 2020.10.01, 23:40

import pathmagic  # noqa # Add parent path to import paths for import config in debug mode

from logger import DEBUG

import imageUtils


def removeImages():
    imageUtils.removeAllImages()


__all__ = [  # Exporting objects...
    'removeImages',
]

if __name__ == '__main__':
    result = removeImages()
    DEBUG('test removeImages', {'result': result})
