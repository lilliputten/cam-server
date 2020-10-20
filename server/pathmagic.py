# -*- coding:utf-8 -*-
# @module pathmagic
# @desc Add parent path to python import paths for testing purposes (allows importing root config module)
# @since 2020.09.29, 22:35
# @changed 2020.10.20, 23:29

import sys
import os
import inspect


rootPath = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
sys.path.insert(0, rootPath)


__all__ = [  # Exporting objects...
    'rootPath',
]
