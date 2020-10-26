# -*- coding:utf-8 -*-
# @module externalApi
# @since 2020.10.26, 03:19
# @changed 2020.10.26, 06:10
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
#  import traceback

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
    #  abort(409)
    #  raise Exception('Test error')
    return jsonify({'error': 'The route \'/api/{route}\' is not implemented for method \'{method}\''.format(*debugData)})


#  class InvalidUsage(Exception):
#      status_code = 400
#      def __init__(self, message, status_code=None, payload=None):
#          Exception.__init__(self)
#          self.message = message
#          if status_code is not None:
#              self.status_code = status_code
#          self.payload = payload
#
#      def to_dict(self):
#          rv = dict(self.payload or ())
#          rv['message'] = self.message
#          return rv
#
#
#  @externalApi.errorhandler(InvalidUsage)
#  def handle_invalid_usage(error):
#      response = jsonify(error.to_dict())
#      response.status_code = error.status_code
#      return response


#  @externalApi.errorhandler(HTTPException)
#  def handle_error(e):
#      """Return JSON instead of HTML for HTTP errors."""
#      # start with the correct headers and status code from the error
#      response = e.get_response()
#      # replace the body with JSON
#      errorData = {
#          'code': e.code,
#          'name': e.name,
#          'description': e.description,
#      }
#      response.data = json.dumps(errorData)
#      DEBUG('externalApi:HTTPException', errorData)
#      return response  # jsonify(errorData)


#  @externalApi.errorhandler(BadRequest)
#  @externalApi.errorhandler(BadRequestKeyError)
#  @externalApi.errorhandler(HTTPException)
#  @externalApi.errorhandler(InternalServerError)
#  @externalApi.errorhandler(MethodNotAllowed)
@externalApi.errorhandler(Exception)
def handle_error(e):
    # TODO: Get error exception description, traceback
    message = getattr(e, 'message', 'Unknown error')
    errorClass = getattr(e, '__class__', '')  # str(e.__class__) if hasattr(e, '__class__') else None
    #  errorTraceback = e.__traceback__ if hasattr(e, '__traceback__') else None
    #  exc_type, exc_value, exc_traceback = sys.exc_info()
    errorData = {
        'message': message,
        'class': str(errorClass),
        'repr': e.__repr__(),
        #  'errorTraceback': errorTraceback,
        #  'e': str(e),
        #  'dir': dir(e),
        #  'e': e.name,
        #  'code': e.code,
        #  'description': e.description,
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
