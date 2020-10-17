#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# @desc Upload image from `local-image.jpg` (created using `client-make-image.sh`) to server
# @since 2020.10.16, 23:31
# @changed 2020.10.17, 03:55
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

# Config parameters...
rootPath = config['rootPath']  # path.dirname(path.abspath(__file__))  # Project root path

# Parameters (real or test)...
remoteUrl = config['remoteUrl'] if '--local' not in sys.argv else 'http://localhost:5000/upload'
localImageFile = config['localImageFile'] if '--test' not in sys.argv else '!Work/200703-rpi-sample-image/image-quarter.jpg'

# Resolve relative file name...
imgFile = path.join(rootPath, localImageFile)

# File handler variable
fh = None

try:
    print('Opening file ' + imgFile)
    fh = open(imgFile, 'rb')
    print('Uploading file to ' + remoteUrl)
    r = requests.post(remoteUrl, files={'file': fh}, auth=HTTPBasicAuth('guest', '123'))
    print(str(r.text).strip())  # Display response
#  except requests.exceptions.RequestException as e:  # Process network error in different way...
#      raise SystemExit(e)
except IOError as e:  # Generic io error...
    raise SystemExit(e)
    #  print('Image file (' + imgFile + ') is not accessible. Use `client-make-image.*` to create it.')
    #  exit(1)
finally:
    if fh:
        fh.close()
