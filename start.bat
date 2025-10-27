@echo off
REM Quick start script for Hindi Document Translator (Windows)

echo ========================================
echo Hindi Document Translator - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Check if font exists
if not exist "fonts\NotoSansDevanagari-Regular.ttf" (
    echo.
    echo WARNING: Hindi font not found!
    echo Please download NotoSansDevanagari-Regular.ttf and place it in the fonts\ directory
    echo Download from: https://fonts.google.com/noto/specimen/Noto+Sans+Devanagari
    echo.
    pause
)

REM Start the application
echo.
echo Starting Hindi Document Translator...
echo.
echo The application will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause
