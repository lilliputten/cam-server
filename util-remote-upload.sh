#!/bin/sh
# @desc Upload/unpack packed raspberry client code to remote device
# @changed 2020.02.06, 12:06

# If no required arguments specified...
if [ $# -ne 1 ]; then
  echo "Usage: $0 <server>"
  exit 1
fi

# Server to upload
SERVER=$1
shift

# Config import
. ./util-config.sh

  # && echo "Creating archive ($ARCNAME)..." \
  # && mkdir -p "$ARCDIR" \
  # && $ARC_CMD "$ARCDIR/$ARCNAME" -C "$SRC" --exclude "*_" --exclude "*.sw?" "*" \

echo "Remote server: $SERVER" \
  && . "./util-local-pack.sh" \
  && echo "Cleaning up remote..." \
  && $PLINK_CMD $SERVER "rm -Rf $REMOTE_TARGET_PATH/$REMOTE_DIR/*" \
  && echo "Making sure that the required remote folders exist..." \
  && $PLINK_CMD $SERVER "mkdir -p -m 0777 $REMOTE_TARGET_PATH/$REMOTE_DIR $REMOTE_TARGET_PATH/$REMOTE_ARCDIR" \
  && echo "Copying archive to remote..." \
  && $CP_CMD "$ARCDIR/$ARCNAME" "$SERVER:$REMOTE_TARGET_PATH/$REMOTE_ARCDIR/" \
  && echo "Extracting archive on remote..." \
  && $PLINK_CMD $SERVER "cd $REMOTE_TARGET_PATH/$REMOTE_DIR && tar xzf \"$REMOTE_TARGET_PATH/$REMOTE_ARCDIR/$ARCNAME\"" \
  && echo "Uploaded $BUILD_TAG"
