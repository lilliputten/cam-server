#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# @desc Get image from camera (using `raspistill`)
# @since 2020.10.16, 23:31
# @changed 2021.05.02, 20:58

#  import sys
from os import path
import os

from config import config

# Using debug
from server.logger import DEBUG

#  DEBUG('Test')

# Config parameters...
rootPath = config['rootPath']  # path.dirname(path.abspath(__file__))  # Project root path

# Create params with resolved image file name...
localImageFile = config['localImageFile']
imgFile = path.join(rootPath, localImageFile)
params = dict(config, **{'imgFile': imgFile})

# Construct command (eg: `raspistill -w 648 -h 486 -o local-image.jpg`)...
command = 'raspistill -w %(imageWidth)d -h %(imageHeight)d -o "%(imgFile)s"' % params

# Executing...
try:
    #  print('Making image using command: ' + command)
    DEBUG('client-make-image: Make image with command', {
        'command': command,
    })
    execResult = os.system(command)
    #  print('Command executing exit code: %d' % execResult)
    DEBUG('client-make-image: Command executing result', {
        'command': command,
        'exit code': execResult,
    })
except IOError as e:  # Generic io error...
    DEBUG('client-make-image: Error catched', {
        'error': e,
        'command': command,
    })
    raise SystemExit(e)

#  # Parameters (real or test)...
#  remoteUrl = config['remoteUrl'] if '--local' not in sys.argv else 'http://localhost:5000/upload'
#  localImageFile = config['localImageFile'] if '--test' not in sys.argv else '!Work/200703-rpi-sample-image/image-quarter.jpg'
