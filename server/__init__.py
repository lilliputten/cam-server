#  from flask import Flask
#  app = Flask('server')

import sys
import os

if os.getenv('FLASK_ENV') == 'development':
    sys.dont_write_bytecode = True
