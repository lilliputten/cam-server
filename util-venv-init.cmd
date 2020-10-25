@echo off
rem @desc Initialize python venv
rem @changed 2020.10.23, 23:41

REM  Global system requirements...
pip install setuptools virtualenv virtualenvwrapper-win
REM  Create venv...
python -m virtualenv -p "C:/Python27/python.exe" .venv
REM  REM  Activate venv
call .venv/Scripts/activate
REM  Install project dependencies...
pip install -r requirements-dev.txt
REM  call .venv/Scripts/deactivate
echo "Use next command to activate venv: 'call .venv/Scripts/activate'"

