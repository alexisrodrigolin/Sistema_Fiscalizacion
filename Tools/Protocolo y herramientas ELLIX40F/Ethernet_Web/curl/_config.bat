set CF_IP=127.0.0.1
set CF_WEBPASS=ABCDEF9876543210

set CURL=curl -s -S --connect-timeout 1 --max-time 10 --user user:%CF_WEBPASS% %CF_IP%

echo Config: %CF_IP% %CF_WEBPASS%
echo.
