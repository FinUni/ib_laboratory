:loop
timeout /t 1
@echo off
for %%i in (*.jpg) do start "" "%%i"&&>nul timeout /t 10
taskkill /F /IM Microsoft.Photos.exe
goto loop