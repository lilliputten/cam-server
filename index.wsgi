# -*- coding: utf-8 -*-

import sys

activate_this = '/home/g/goldenjeru/.venv-flask/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

sys.path.insert(1,'/home/g/goldenjeru/lilliputten.ru/cam/')

from server.server import app as application
