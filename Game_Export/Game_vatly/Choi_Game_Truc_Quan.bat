@echo off
title SINE Game Web Player
echo Dang khoi dong may chu ao de choi game...
start http://localhost:8000
python -m http.server 8000
