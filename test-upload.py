import requests
import sys

# http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

localUrl = 'http://localhost:5000/upload/tag'
remoteUrl = 'https://cam.lilliputten.ru/upload/tag'

url = remoteUrl if '--remote' in sys.argv else localUrl

fin = open('test-image.jpg', 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print r.text
finally:
    fin.close()
