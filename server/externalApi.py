# -*- coding:utf-8 -*-
# @module externalApi
# @since 2020.10.26, 03:19
# @changed 2020.10.26, 18:03
#
#  Basic api structure (from `README.md`):
#
#  - GET `/api/images`: Get all images list.
#  - GET `/api/images/recent`: Get recent image info.
#  - GET `/api/images/{id}`: Get specific image info.
#  - POST `/api/images/add`: Add (upload) new image. (Duplicates `/upload`?)
#  - DELETE `/api/images`: Delete all images.
#  - DELETE `/api/images/{id}`: Delete specific image.

import pathmagic  # noqa

#  import sys
import traceback

from flask import Blueprint
from flask import jsonify
#  from flask import json
#  from flask import abort
from flask import request

#  from werkzeug.exceptions import BadRequest
#  from werkzeug.exceptions import BadRequestKeyError
#  from werkzeug.exceptions import HTTPException
#  from werkzeug.exceptions import InternalServerError
#  from werkzeug.exceptions import MethodNotAllowed
#  from werkzeug.exceptions import default_exceptions

#  from config import config

from logger import DEBUG

import imageUtils


externalApi = Blueprint('api', __name__)


@externalApi.route('/api/test')
def test():
    return jsonify({'test': 'Ok'})


@externalApi.route('/api/images')
def listAllImages():
    list = imageUtils.loadImagesList(True)
    DEBUG('externalApi:listAllImages called (/api/images)', {
        'list': list,
    })
    if not list:
        list = []
    return jsonify(list)


@externalApi.route('/api/images/<id>')
def getImageData(id):
    list = imageUtils.loadImagesList(True)
    DEBUG('externalApi:getImageData called (/api/images/' + id + ')', {
        'id': id,
        'list': list,
    })
    for index, data in enumerate(list):
        if data['id'] == id:
            DEBUG('externalApi:getImageData called (/api/images/' + id + ')', {
                'id': id,
                'list': list,
            })
            return jsonify(data)
    return jsonify({'error': 'No image found for id ' + id})


@externalApi.route('/api/images/last')
@externalApi.route('/api/images/recent')
def getRecentImageData():
    data = imageUtils.getRecentImageData()
    DEBUG('externalApi:getRecentImageData called (/api/images/recent)', {
        'data': data,
    })
    return jsonify(data)


@externalApi.route('/api/<path:route>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def fallback(route):
    debugData = {
        'route': route,
        'method': request.method,
    }
    DEBUG('externalApi:fallback', debugData)
    errorStr = 'The route \'/api/{route}\' is not implemented for method \'{method}\''.format(**debugData)
    return jsonify({'error': errorStr})


#  @externalApi.errorhandler(BadRequest)
#  @externalApi.errorhandler(BadRequestKeyError)
#  @externalApi.errorhandler(HTTPException)
#  @externalApi.errorhandler(InternalServerError)
#  @externalApi.errorhandler(MethodNotAllowed)
@externalApi.errorhandler(Exception)
def handle_error(e):
    #  errorType, errorValue, errorTraceback = sys.exc_info()
    #  @see https://docs.python.org/2/library/traceback.html
    errorTraceback = traceback.format_exc()
    errorData = {
        'error': 'Internal exception: ' + e.__repr__(),
        #  'type': str(errorType),
        'traceback': str(errorTraceback)
    }
    DEBUG('externalApi:Exception', errorData)
    return jsonify(errorData), getattr(e, 'code', 500)


__all__ = [  # Exporting objects...
    'externalApi',
]

if __name__ == '__main__':
    pass
    #  app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    #  app.logger.debug('test log')
    #  # app.debug = True
    #  app.run()
