#!/bin/sh
# @desc Sort builds in current folder
# @since 2020.02.06, 17:35
# @changed 2020.07.17, 15:18

# # Config import
# . ./util-config.sh
# echo "Sorting builds in $ARCDIR"
# test -d "$ARCDIR" || mkdir -p "$ARCDIR"
# cd "$ARCDIR"

echo "Sort builds in current folder..."
# NOTE: for Windows must be using some POSIX (cygnus, eg) find command instead default Win32 version
FILES=`find_ . -maxdepth 1 -type f -name "*.tgz"`
COUNT=0
for F in $FILES; do
  # Extract date tag form filename in format '*-v.X.Y.Z-YYMMDD-HHMM-*'
  D=`echo $F | sed 's/^.*-\(v[0-9a-z.]\+\)-\([0-9]\+\)-.*$/\2/'`
  test -d "./$D" || mkdir -p "./$D"
  echo "$F --> $D"
  mv "$F" "./$D/"
  COUNT=$(expr $COUNT + 1)
done
echo "Processed files: $COUNT"
