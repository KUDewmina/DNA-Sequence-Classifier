@echo off
title DNA Classifier - Auto Setup Installer
cls
echo ======================================================
echo            DNA Classifier - Auto Setup
echo ======================================================

set PY_VERSION=3.11.0
set PY_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
set INSTALLER=python311.exe

echo Checking for Python %PY_VERSION%...
py -3.11 --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python 3.11 found!
    goto CREATE_VENV
)

echo Python 3.11 NOT FOUND. Downloading installer...
powershell -command "(New-Object Net.WebClient).DownloadFile('%PY_URL%', '%INSTALLER%')"

echo Installing Python 3.11 silently...
%INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Installation complete. Updating PATH...
setx PATH "%PATH%;C:\Program Files\Python311\;C:\Program Files\Python311\Scripts\" >nul

echo Re-checking Python installation...
py -3.11 --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python 3.11 installation failed.
    pause
    exit /b
)

:CREATE_VENV
echo ------------------------------------------------------
echo Creating virtual environment...
echo ------------------------------------------------------
py -3.11 -m venv venv

echo Activating venv...
call venv\Scripts\activate

echo Upgrading pip...
pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt


echo ------------------------------------------------------
echo  Starting Flask app in a new window...
echo ------------------------------------------------------
start "DNA Classifier Server" cmd /k "call venv\Scripts\activate && python dna_classifier.py"

echo Waiting for Flask server to start...

:: ---- FUNCTION: WAIT FOR SERVER ----
:WAIT_FOR_SERVER
powershell -command "(Invoke-WebRequest -Uri 'http://127.0.0.1:5000' -UseBasicParsing -TimeoutSec 1)" >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Server is ready!
    goto SERVER_READY
)
timeout /t 1 >nul
goto WAIT_FOR_SERVER

:SERVER_READY
echo Opening browser...
start "" http://127.0.0.1:5000

echo ------------------------------------------------------
echo   Setup Complete! Flask app is now running.
echo ------------------------------------------------------
pause
exit /b
