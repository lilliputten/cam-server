@echo off
rem @desc Initialize python venv
rem @changed 2020.10.19, 03:30

python -m virtualenv -p "C:/Python27/python.exe" .venv
REM  call .venv/Scripts/activate
pip install -r requirements-dev.txt
REM  call .venv/Scripts/deactivate

