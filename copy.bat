@echo off
setlocal

rem Exit on error
set ERRORLEVEL=0

rem Copy .env files within the Jenkins workspace
copy /Y "C:\jenkins_home\workspace\proj6\uc1\.env" "C:\jenkins_home\workspace\proj6\uc1\"
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

copy /Y "C:\jenkins_home\workspace\proj6\uc2\.env" "C:\jenkins_home\workspace\proj6\uc2\"
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

copy /Y "C:\jenkins_home\workspace\proj6\uc3\.env" "C:\jenkins_home\workspace\proj6\uc3\"
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

endlocal
