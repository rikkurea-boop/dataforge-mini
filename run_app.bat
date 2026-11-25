@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo === Starting DataForge Mini ===

if exist ".venv\Scripts\python.exe" goto :run_app

echo Creating virtual environment (.venv) and installing dependencies...
py -3.13 -m venv .venv 2>nul
if exist ".venv\Scripts\python.exe" goto :install_deps

py -3 -m venv .venv 2>nul
if exist ".venv\Scripts\python.exe" goto :install_deps

python -m venv .venv 2>nul
if exist ".venv\Scripts\python.exe" goto :install_deps

echo Error: Python 3 not found. Please install Python 3.11 - 3.13 from https://www.python.org/downloads/
pause
exit /b 1

:install_deps
".venv\Scripts\python.exe" -m pip install numpy pandas matplotlib streamlit
if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

:run_app
echo Opening app in browser (http://localhost:8501)...
echo Press Ctrl + C in this window to stop the app.
".venv\Scripts\python.exe" -m streamlit run app.py
if errorlevel 1 pause
