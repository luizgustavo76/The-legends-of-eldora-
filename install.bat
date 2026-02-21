@echo off
echo Instalando TLOE...

set DEST=%USERPROFILE%\the legends of eldora alpha 4
mkdir "%DEST%"

xcopy /E /I /Y "%~dp0game\*" "%DEST%"

echo Instalado!
pause