#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import sys

# http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

localUrl = 'http://localhost:5000/upload'
remoteUrl = 'https://cam.lilliputten.ru/upload'

url = remoteUrl if '--remote' in sys.argv else localUrl

#  imgFile = 'test-image.jpg'
imgFile = '!Work/200703-rpi-sample-image/image-quarter.jpg'
fin = open(imgFile, 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print r.text
finally:
    fin.close()
