#!/bin/sh
# @desc Initialize python venv
# @changed 2020.10.19, 03:30

if uname | grep -q "CYGWIN"; then
  cmd /C "util-venv-init.cmd"
else
  python -m virtualenv -p "/usr/bin/python2.7" .venv
  . ./.venv/Scripts/activate
  pip install -r requirements-dev.txt
fi
