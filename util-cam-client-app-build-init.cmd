@echo off
rem @desc Initialize `cam-client-app-build` link
rem @changed 2020.10.21, 04:55

REM echo Using entire build repository
REM linkd "cam-client-app-build" "../cam-client-app-build"

echo Using publish folder of source repository
linkd "cam-client-app-build" "../cam-client-app/publish"
