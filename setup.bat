@echo off
title SHOP2SCA - Setup
echo Installing dependencies...
@pip install requests pyautogui colorama >nul 2>&1
if errorlevel 1 (
    echo Failed to install dependencies. Check Python/pip.
    pause
    exit
)
echo Setup completed. Run run.bat
pause