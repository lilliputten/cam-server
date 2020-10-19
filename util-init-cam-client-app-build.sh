#!/bin/sh
# @desc Initialize `cam-client-app-build` link
# @changed 2020.10.19, 03:26

if uname | grep -q "CYGWIN"; then
  cmd /C "util-init-cam-client-app-build.cmd"
else
  ln -s "../../../cam-client-app-build" "server/static/cam-client-app-build"
fi
