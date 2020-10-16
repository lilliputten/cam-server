#!/bin/sh
# @desc Create archive for upload
# @changed 2020.10.17, 00:56

# # If no required arguments specified...
# if [ $# -ne 1 ]; then
#   echo "Usage: $0 <build-type>"
#   echo "Eg: $0 dev"
#   exit 1
# fi

# Config import
. ./util-config.sh

# # Source build path
# SRCDIR="$PROJECT_NAME"
# shift
# # Example command: && $ARC_CMD "$ARCDIR/$ARCNAME" -C "$SRCDIR" \ # Change to dir

echo "Creating archive: '$ARCNAME' in folder '$ARCDIR'..." \
&& mkdir -p "$ARCDIR" \
&& $ARC_CMD "$ARCDIR/$ARCNAME" \
  --exclude "*.pyc" \
  --exclude "*.bak" --exclude "*.tmp" --exclude "*~"  --exclude "*_" --exclude "*.sw?" \
  --exclude "static" --exclude "templates" \
  "build-tag*" \
  "client-*" \
  "config*" \
  "*.md" \
  "server/*" \
&& echo OK
