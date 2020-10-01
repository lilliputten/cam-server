# -*- coding:utf-8 -*-
# @module app
# @since 2020.07.04, 01:43
# @changed 2020.07.04, 01:43

import os

from flask import Flask
#  from view import tags

app = Flask(__name__)


@app.template_filter()
def getenv(key):
    return os.getenv(key)


#  environment.filters['env_override'] = env_override


__all__ = [  # Exporting objects...
    'app',
]
