#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}===================================================${NC}"
echo -e "          LINUX BUILD ISLEMI BASLIYOR"
echo -e "${BLUE}===================================================${NC}"
echo ""

# Scriptin çalıştığı yerdeki Client klasörüne geçiş yap
cd "$(dirname "$0")/Client" 2>/dev/null || cd "Client"

# pyinstaller sistemde yüklüyse derlemeyi tetikler
if command -v pyinstaller &> /dev/null; then
    pyinstaller --onefile main.py
    echo ""
    echo -e "${GREEN}[OK] Linux build tamamlandi! Ciktilar dist/ klasöründe.${NC}"
else
    echo "Hata: Sistemde 'pyinstaller' bulunamadi."
    echo "Kurmak icin: pip install pyinstaller"
fi

echo -e "${BLUE}===================================================${NC}"