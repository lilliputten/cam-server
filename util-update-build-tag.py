# -*- coding:utf-8 -*-
# @module util-update-build-tag
# @since 2020.02.23, 00:58
# @changed 2020.02.23, 01:58

import json
import datetime
import os
from os import path


rootPath = os.getcwd()

buildTagFilename = path.join(rootPath, 'build-tag.txt')
packageFilename = path.join(rootPath, 'package.json')

dateTagFormat = '%y%m%d-%H%M'
#  shortDateFormat = '%Y.%m.%d-%H:%M'
#  detailedDateFormat = shortDateFormat + ':%S.%f'

now = datetime.datetime.now()
dateTag = now.strftime(dateTagFormat)

pkgConfigFile = open(packageFilename)
pkgConfig = json.load(pkgConfigFile)
pkgConfigFile.close()

version = pkgConfig['version']

buildTag = 'v.' + version + '-' + dateTag

print 'Updated build tag:', buildTag

with open(buildTagFilename, 'w') as file:
    file.write(buildTag)
    file.close()
