#!/bin/sh
# @desc Test remote raspberry client connection
# @since 2021.05.02, 19:20
# @changed 2021.05.02, 19:20

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

CMD_MKDIR="$PLINK_CMD $SERVER \"mkdir -p -m 0777 $REMOTE_TARGET_PATH/$REMOTE_DIR $REMOTE_TARGET_PATH/$REMOTE_ARCDIR\""
echo "Remote server: $SERVER" \
  && echo $PLINK_CMD $SERVER "mkdir -p -m 0777 $REMOTE_TARGET_PATH/$REMOTE_DIR $REMOTE_TARGET_PATH/$REMOTE_ARCDIR" \
  && $PLINK_CMD $SERVER "mkdir -p -m 0777 $REMOTE_TARGET_PATH/$REMOTE_DIR $REMOTE_TARGET_PATH/$REMOTE_ARCDIR" \
  && echo "Done: testing"
  # && echo "Test mkdir: $CMD_MKDIR" \
  # && $CMD_MKDIR \
  # && echo "XXX: $PLINK_CMD $SERVER \"mkdir -p -m 0777 $REMOTE_TARGET_PATH/$REMOTE_DIR $REMOTE_TARGET_PATH/$REMOTE_ARCDIR\"" \
