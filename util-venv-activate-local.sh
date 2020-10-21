#!/bin/sh

if uname | grep -q "CYGWIN"; then
  cmd /C "util-venv-activate-local.cmd"
else
  source "./.venv/Scripts/activate"
fi
