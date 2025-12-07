@echo off
echo ===========================================
echo     DNA Classifier - Auto Setup Installer
echo ===========================================
set PY_VERSION=3.11.0
set PY_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
set INSTALLER=python311.exe

:: Check if Python 3.11 is installed
py -3.11 --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python 3.11 found!
    goto CREATE_VENV
)

echo Python 3.11 NOT FOUND. Downloading installer...
powershell -command "(New-Object Net.WebClient).DownloadFile('%PY_URL%', '%INSTALLER%')"

echo Installing Python 3.11 silently...
%INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Installation complete. Refreshing environment...
setx PATH "%PATH%;C:\Program Files\Python311\;C:\Program Files\Python311\Scripts\"

:: Check again
py -3.11 --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python 3.11 installation failed.
    pause
    exit /b
)

:CREATE_VENV
echo Creating virtual environment...
py -3.11 -m venv venv

echo Activating venv...
call venv\Scripts\activate

echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

echo Opening the application in your browser...
start "" http://127.0.0.1:5000

echo Starting Flask app...
python dna_classifier.py
