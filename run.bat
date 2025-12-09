@echo off
TITLE Virtual AI Mouse

:: Check if venv exists
IF NOT EXIST "venv" (
    ECHO Error: Virtual environment not found!
    ECHO Please run 'setup.bat' first.
    PAUSE
    EXIT
)

ECHO Activating Virtual Environment...
call venv\Scripts\activate

ECHO Starting AI Mouse...
python src/main.py

ECHO Closing...
call deactivate