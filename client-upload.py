#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# @desc Upload image from `local-image.jpg` (created using `client-make-image.sh`) to server
# @since 2020.10.16, 23:31
# @changed 2021.05.02, 20:48
#
# TODO:
# - Use config parameters for image file name and remote url?
# - Get url from command line?
# README:
# - http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

import requests
from requests.auth import HTTPBasicAuth
import sys
from os import path

from config import config
#  from .logger import DEBUG
from server.logger import DEBUG

# Config parameters...
rootPath = config['rootPath']  # path.dirname(path.abspath(__file__))  # Project root path

# Parameters (real or test)...
remoteUrl = config['remoteUrl'] if '--local' not in sys.argv else 'http://localhost:5000/upload'
localImageFile = config['localImageFile'] if '--test' not in sys.argv else '!Work/200703-rpi-sample-image/image-quarter.jpg'

# Resolve relative file name...
imgFile = path.join(rootPath, localImageFile)

# File handler variable
fh = None

#  # Test debug...
#  DEBUG('Client started', {
#      'buildTag': config['buildTag'],
#  })

try:
    #  print('Opening file ' + imgFile)
    DEBUG('client-upload: Opening file', {
        'imgFile': imgFile,
    })
    fh = open(imgFile, 'rb')
    #  print('Uploading file to ' + remoteUrl)
    DEBUG('client-upload: Uploading file', {
        'remoteUrl': remoteUrl,
        'imgFile': imgFile,
    })
    # TODO: To store auth params in system variables?
    r = requests.post(remoteUrl, files={'file': fh}, auth=HTTPBasicAuth('guest', '123'))
    result = str(r.text).strip()
    print(result)  # Display response
    DEBUG('client-upload: File uploaded', {
        'remoteUrl': remoteUrl,
        'imgFile': imgFile,
        'result': result,
    })
#  except requests.exceptions.RequestException as e:  # Process network error in different way...
#      raise SystemExit(e)
except IOError as e:  # Generic io error...
    #  print('Image file (' + imgFile + ') is not accessible. Use `client-make-image.*` to create it.')
    DEBUG('client-upload: Error catched', {
        'error': e,
        'imgFile': imgFile,
        'remoteUrl': remoteUrl,
    })
    raise SystemExit(e)
    #  print('Image file (' + imgFile + ') is not accessible. Use `client-make-image.*` to create it.')
    #  exit(1)
finally:
    if fh:
        fh.close()
