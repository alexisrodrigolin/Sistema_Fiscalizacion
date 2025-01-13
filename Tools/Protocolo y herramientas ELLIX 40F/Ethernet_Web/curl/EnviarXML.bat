@echo off
cd /d %~dp0

call _config.bat

set XML_FILE=%1

%CURL%/ifcmd.xml --data-binary @%XML_FILE% --header "Content-Type: text/xml" > _lastres.xml
if not %ERRORLEVEL% equ 0 goto error

echo.
type _lastres.xml

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
