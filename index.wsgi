# -*- coding: utf-8 -*-

import sys

activate_this = '/home/g/goldenjeru/.virtualenv/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

sys.path.insert(1,'/home/g/goldenjeru/cam.lilliputten.ru/')

from flask_project.hello import app as application