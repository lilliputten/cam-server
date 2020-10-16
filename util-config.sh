#!/bin/sh
# @desc Remote utils configuration
# @changed 2020.10.16, 22:41

export DATE=`date "+%Y.%m.%d %H:%M:%S"`
export DATETAG=`date "+%y%m%d-%H%M"`

export PWD=`pwd`
# export PROJECT_NAME=`basename "${PWD}"`
export PROJECT_NAME="cam-client"

export ARCDIR="../!ARC"
export REMOTE_ARCDIR="!ARC"

test -z "$SRC" && SRC="."

export BUILD_TAG=`cat "$SRC/build-tag.txt" 2>&1`

# Check for creditinals presence...
export CamRpiPort="22" # Terminal connection port (may be sepcified in environment)
# Note: `$CamRpiUser` and `$CamRpiPw` taken from project environment
if [ -z "$CamRpiUser" -o -z "$CamRpiPw" -o -z "$CamRpiPort" ]; then
  echo "Terminal creditinals must be specified in system environment!"
  echo "Check/set system environment variables 'CamRpiUser' and 'CamRpiPw'."
  exit 1
fi

# Commands configuration...
export PLINK_CMD="plink -C -P $CamRpiPort -l $CamRpiUser -pw $CamRpiPw"
export CP_CMD="pscp -scp -r -C -P $CamRpiPort -l $CamRpiUser -pw $CamRpiPw"

export ARC_CMD="tar czf"

export REMOTE_TARGET_PATH="/home/pi" # Destination folder
export REMOTE_DIR="$PROJECT_NAME" # "cam-client" # Destination folder

export ARCNAME="$PROJECT_NAME-$BUILD_TAG.tgz"
