#!/bin/sh
# @desc Initialize `cam-client-app-build` link
# @changed 2020.10.20, 23:33

if uname | grep -q "CYGWIN"; then
  cmd /C "util-cam-client-app-build-init.cmd"
else
  ln -s "../cam-client-app-build" "./cam-client-app-build"
fi
