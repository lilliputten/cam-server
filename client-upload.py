#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# @desc Upload image from `local-image.jpg` (created using `client-make-image.sh`) to server
# @since 2020.10.16, 23:31
# @changed 2020.10.16, 23:31
#
# TODO:
# - Use config parameters for image file name and remote url?
# - Get url from command line?
# README:
# - http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

import requests
import sys

from config import config

# Parameters (real or test)...
url = config['remoteUrl'] if '--local' not in sys.argv else 'http://localhost:5000/upload'
imgFile = config['localImageFile'] if '--test' not in sys.argv else '!Work/200703-rpi-sample-image/image-quarter.jpg'

fh = None  # File handler

try:
    print('Opening file ' + imgFile)
    fh = open(imgFile, 'rb')
    print('Uploading file to ' + url)
    r = requests.post(url, files={'file': fh})
    print(r.text)  # Display response
#  except requests.exceptions.RequestException as e:  # Process network error in different way...
#      raise SystemExit(e)
except IOError as e:  # Generic io error...
    raise SystemExit(e)
    #  print('Image file (' + imgFile + ') is not accessible. Use `client-make-image.*` to create it.')
    #  exit(1)
finally:
    if fh:
        fh.close()
