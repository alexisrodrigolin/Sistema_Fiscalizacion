@echo off
cd /d %~dp0

call _config.bat

set JSON_FILE=%1

%CURL%/ifcmd.json --data-binary @%JSON_FILE% --header "Content-Type: application/json" > _lastres.json
if not %ERRORLEVEL% equ 0 goto error

echo.
type _lastres.json

goto end

:error
echo.
echo Error
echo.
goto end

:end
echo.
echo.
pause
