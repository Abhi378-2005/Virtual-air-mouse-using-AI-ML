@echo off
TITLE Setting up Virtual Mouse Environment...

ECHO ==========================================
ECHO 1. Creating Virtual Environment (venv)...
ECHO ==========================================
python -m venv venv

ECHO.
ECHO ==========================================
ECHO 2. Activating Environment...
ECHO ==========================================
call venv\Scripts\activate

ECHO.
ECHO ==========================================
ECHO 3. Installing Dependencies...
ECHO ==========================================
pip install -r requirements.txt

ECHO.
ECHO ==========================================
ECHO Setup Complete! You can now use run.bat
ECHO ==========================================
PAUSE