#!/bin/sh
# @desc Execute command on remote raspberry device
# @changed 2020.02.06, 14:27

# If no arguments specified...
if [ $# -lt 2 ]; then
  echo "Usage: $0 <server> <cmd...>"
  exit 1
fi

# Remote server
SERVER=$1
shift

# Config import
. ./util-config.sh

echo "Running commands ($*) on $SERVER..." \
  && $PLINK_CMD $SERVER "cd $REMOTE_TARGET_PATH; $*"
