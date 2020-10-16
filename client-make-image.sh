#!/bin/sh
# @desc Make camera shot to `local-image.jpg`
# @since 2020.10.16, 23:31
# @changed 2020.10.16, 23:31
# TODO!

# py client-make-image.py $@
raspistill -w 648 -h 486 -o local-image.jpg
