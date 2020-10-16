#!/bin/sh
# @desc Enable ssh on remote server
# @changed 2020.06.30, 08:46

# If no arguments specified...
if [ $# -ne 1 ]; then
  echo "Usage: $0 <server>"
  exit 1
fi

echo "SSH constantly enabled"

# # Remote server
# SERVER="$1"
#
# echo "Enabling SSH on $SERVER..."
# if wget -t 1 -T 3 -O- --progress=dot:default --no-check-certificate https://$SERVER:11111/ssh_on; then
#   echo "SSH enabled"
#   echo "------------------------------------------------------------"
# else
#   echo "SSH enabling failed!"
#   exit -1
# fi
