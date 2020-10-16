#!/bin/sh
# @desc Make & upload camera shot
# @since 2020.10.16, 23:31
# @changed 2020.10.17, 02:37

BASEDIR=`dirname "$0"`
case `uname` in
    *CYGWIN*) BASEDIR=`cygpath -w "$BASEDIR"`;;
esac

MAKE_IMG_CMD="python $BASEDIR/client-make-image.py"
# MAKE_IMG_CMD="raspistill -w 648 -h 486 -o local-image.jpg"

$MAKE_IMG_CMD \
  && python $BASEDIR/client-upload.py \
  && echo OK

  # && rm -f $BASEDIR/local-image.* \
