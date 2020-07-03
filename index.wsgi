# -*- coding: utf-8 -*-
# @module index.wsgi
# @since 2019.03.28, 21:32
# @changed 2019.03.28, 23:07

import sys

activate_this = '/home/g/goldenjeru/.venv-flask/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

sys.path.insert(1,'/home/g/goldenjeru/lilliputten.ru/cam/')

from server.app import app as application
