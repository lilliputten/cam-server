# -*- coding: utf-8 -*-
# vim: ft=python:
# @module index.wsgi
# @since 2019.03.28, 21:32
# @changed 2020.07.04, 01:47

import sys
import os

activate_this = '/home/g/goldenjeru/.venv-flask/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

global ROOT_PATH
ROOT_PATH = os.getcwd()

sys.path.insert(1, ROOT_PATH)
# sys.path.insert(1,'/home/g/goldenjeru/lilliputten.ru/cam/')

from server.server import app as application  # noqa
