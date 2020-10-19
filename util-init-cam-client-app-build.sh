#!/bin/sh
# @desc Initialize `cam-client-app-build` link
# @changed 2020.10.19, 03:05

if uname | grep -q "CYGWIN"; then
  cmd /C "util-init-cam-client-app-build.cmd"
else
  ln -s "server/static/cam-client-app-build" "../cam-client-app-build"
fi
