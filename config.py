# -*- coding:utf-8 -*-
# @module config
# @since 2020.02.23, 02:18
# @changed 2020.04.23, 03:48
# See:
#  - https://docs.python.org/3/library/configparser.html -- ???
#  - https://stackoverflow.com/questions/9590382/forcing-python-json-module-to-work-with-ascii

#  from flask import current_app as app
#  from flaskapp import app

from os import path
import json
import yaml

#  rootPath = getcwd()
#  libPath = app.root_path
#  rootPath = path.dirname(libPath)
#  rootPath = ROOT_PATH  # From index.wsgi
rootPath = path.dirname(path.abspath(__file__))  # From index.wsgi
print 'rootPath: ' + rootPath

yamlConfigFilename = path.join(rootPath, 'config.yml')
yamlLocalConfigFilename = path.join(rootPath, 'config.local.yml')

buildTagFilename = path.join(rootPath, 'build-tag.txt')
packageFilename = path.join(rootPath, 'package.json')
#  print 'config: packageFilename', packageFilename  # DEBUG

version = 'Testing'
buildTag = 'Testing'

if path.isfile(packageFilename):
    pkgConfigFile = open(packageFilename)
    pkgConfig = json.load(pkgConfigFile)
    version = pkgConfig['version'].encode('ascii')
    pkgConfigFile.close()

if path.isfile(buildTagFilename):
    buildTagFile = open(buildTagFilename, 'r')
    buildTag = buildTagFile.read()
    buildTagFile.close()

config = {  # Default config
    'version': version,
    'buildTag': buildTag,
    #  'libPath': libPath,
    'rootPath': rootPath,
    'uploadPath': path.join(rootPath, 'uploads'),
    'channelsDir': 'channels',
    'outputLog': True,
    'outputColoredLog': True,
    'writeLog': True,
    'clearLogFile': False,
    'dateTagFormat': '%y%m%d-%H%M',
    'shortDateFormat': '%Y.%m.%d-%H:%M',
    'logDateFormat': '%y%m%d-%H%M%S-%f',
    'detailedDateFormat': '%Y.%m.%d-%H:%M:%S.%f',
    'testList': [
        1,
        2,
        [
            3,
            4,
        ],
    ],
    #  'collectorFileName': 'collector.txt',  # Add to gitignore
}


def updateConfigWithYaml(config, file):
    """
    Extend config from file
    """
    if path.isfile(file):
        with open(file) as file:
            #  print 'Extending config with', file
            yamlConfigData = yaml.load(file, Loader=yaml.FullLoader)
            #  print 'yamlConfigData:', yamlConfigData
            config.update(yamlConfigData)


updateConfigWithYaml(config, yamlConfigFilename)
updateConfigWithYaml(config, yamlLocalConfigFilename)
