@echo off
REM SEO Max - Python Environment Setup Script (Windows)
REM Automatically creates virtual environment and installs dependencies

setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "VENV_DIR=%SCRIPT_DIR%.venv"

echo 🚀 SEO Max - Python Setup
echo.

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Error: Python 3 is not installed
    echo.
    echo Install Python 3.8+ first:
    echo   winget install Python.Python.3.12
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Found Python %PYTHON_VERSION%

REM Create virtual environment if it doesn't exist
if not exist "%VENV_DIR%" (
    echo 📦 Creating virtual environment...
    python -m venv "%VENV_DIR%"
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"

REM Upgrade pip
echo 📥 Upgrading pip...
pip install --quiet --upgrade pip

REM Install dependencies
echo 📥 Installing dependencies from requirements.txt...
pip install --quiet -r "%SCRIPT_DIR%requirements.txt"

echo.
echo ✅ Setup complete!
echo.
echo To activate the virtual environment manually:
echo   %VENV_DIR%\Scripts\activate.bat
echo.
echo To run analyzers:
echo   python scripts\page_analyzer.py https://example.com
echo   python scripts\schema_validator.py https://example.com
echo   python scripts\insights_optimizer.py https://example.com
echo   python scripts\sitemap.py https://example.com/sitemap.xml
echo   python scripts\site_crawler.py https://example.com
echo.

endlocal
