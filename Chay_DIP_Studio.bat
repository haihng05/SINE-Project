@echo off
title SINE DIP Studio Viewer
cd /d "%~dp0"
echo ========================================================
echo   KHOI DONG DIP STUDIO (XU LY VA TRUC QUAN HOA ANH DE THI)
echo ========================================================
echo Dang mo giao dien DIP Studio...
.\venv\Scripts\python.exe tools\dip_viewer_gui.py --image test_images\test.png
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Co loi xay ra khi chay chuong trinh!
    pause
)
