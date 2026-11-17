@echo off
title SINE Educational Game Generator
cd /d "%~dp0"
echo ========================================================
echo   KHOI DONG GIAO DIEN HE THONG SINE (CO MODULE XU LY ANH DIP)
echo ========================================================
echo Dang mo giao dien...
.\venv\Scripts\python.exe sine_gui.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Co loi xay ra khi chay chuong trinh!
    pause
)
