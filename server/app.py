# -*- coding:utf-8 -*-
# @module app
# @since 2020.07.04, 01:43
# @changed 2020.10.20, 23:29

import pathmagic  # noqa

import os

from flask import Flask

from config import config


#  rootPath = config['rootPath']
#  clientStaticPath = config['clientStaticPath']
clientTemplatePath = config['clientTemplatePath']

app = Flask(__name__,
            static_url_path='',
            static_folder=clientTemplatePath)


@app.template_filter()
def getenv(key):
    return os.getenv(key)


__all__ = [  # Exporting objects...
    'app',
]
