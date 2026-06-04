@echo off
title ToGoSOURCE Core Engine
color 0B
cls

:: Client klasörünü hedef gösteriyoruz
cd /d "D:\ToGoSOURCE\Client"

:menu
cls
echo ===================================================
echo             TOGOSOURCE CORE ENGINE v1.0
echo ===================================================
echo  [1] Check Status (git status)
echo  [2] Commit and Push (Save to Local GitHub)
echo  [3] Pull Changes from Server (Update)
echo  [4] View Commit History (git log)
echo  [5] Exit
echo ===================================================
set /p choice="Select an option (1-5): "

if "%choice%"=="1" goto status
if "%choice%"=="2" goto push
if "%choice%"=="3" goto pull
if "%choice%"=="4" goto log
if "%choice%"=="5" exit
goto menu

:status
cls
echo === WORKING DIRECTORY STATUS ===
git status
echo.
pause
goto menu

:push
cls
echo === SAVING CHANGES TO SERVER ===
git add .
set /p msg="Enter Commit Message: "
if "%msg%"=="" set msg="Minor updates"

git commit -m "%msg%"
echo.
echo Sending files to Server (Remote)...
git push origin main
echo.
echo [SUCCESS] Project backed up to Server!
pause
goto menu

:pull
cls
echo === PULLING LATEST CHANGES FROM SERVER ===
git pull origin main
echo.
pause
goto menu

:log
cls
echo === RECENT COMMIT HISTORY ===
git log --oneline -n 10
echo.
pause
goto menu