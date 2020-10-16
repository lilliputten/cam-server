#!/bin/sh
# @desc Create archive for upload
# @changed 2020.10.16, 22:57

# # If no required arguments specified...
# if [ $# -ne 1 ]; then
#   echo "Usage: $0 <build-type>"
#   echo "Eg: $0 dev"
#   exit 1
# fi
# # Source build path
# SRCDIR="cam-client-$1"
# shift

# # Source build path
# SRCDIR="cam-client"
# && $ARC_CMD "$ARCDIR/$ARCNAME" -C "$SRCDIR" \ # Change to dir

# Config import
. ./util-config.sh

echo "Creating archive: '$ARCNAME' in folder '$ARCDIR'..." \
&& mkdir -p "$ARCDIR" \
&& $ARC_CMD "$ARCDIR/$ARCNAME" \
  --exclude "*.pyc" --exclude "*.bak" --exclude "*.tmp" --exclude "*~"  --exclude "*_" --exclude "*.sw?" \
  "build-tag*" \
  "client-*" \
  "config*" \
  "*.md" \
&& echo OK
