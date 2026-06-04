@echo off
title Download TOGOSOURCE1 to Downloads
color 0A
cls

:: Bilgisayarındaki Downloads (İndirilenler) klasörüne geçiş yapıyoruz
cd /d "%USERPROFILE%\Downloads"

echo ===================================================
echo          DOWNLOADING PROJ FROM GITHUB
echo ===================================================
echo Downloading into: %USERPROFILE%\Downloads\TOGOSOURCE1-Main
echo.

:: Eğer önceden indirildiyse çakışmaması için eski klasörü temizler
if exist "TOGOSOURCE1-Main" rd /s /q "TOGOSOURCE1-Main"

:: GitHub'daki güncel kodları doğrudan indirilenler klasörüne klonlar
git clone https://github.com/kanbermustafakerem-collab/TOGOSOURCE1.git TOGOSOURCE1-Main

echo.
echo ===================================================
echo [SUCCESS] Project downloaded successfully to Downloads!
echo ===================================================
pause