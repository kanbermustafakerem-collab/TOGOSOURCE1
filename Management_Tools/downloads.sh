#!/bin/bash

# Renklendirme tanımları
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # Renksiz

echo -e "${BLUE}===================================================${NC}"
echo -e "          GITHUB'DAN PROJE INDIRILIYOR"
echo -e "${BLUE}===================================================${NC}"

# Kullanıcının Downloads klasörünü bul ve oraya geç
TARGET_DIR="$HOME/Downloads"
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

echo -e "Hedef Klasor: $TARGET_DIR/TOGOSOURCE1-Main"
echo ""

# Eski klasör varsa çakışmaması için temizle
if [ -d "TOGOSOURCE1-Main" ]; then
    rm -rf "TOGOSOURCE1-Main"
fi

# Canlı depodan güncel kodları çekiyoruz
git clone https://github.com/kanbermustafakerem-collab/TOGOSOURCE1.git TOGOSOURCE1-Main

echo ""
echo -e "${BLUE}===================================================${NC}"
echo -e "${GREEN}[BASARILI] Proje Downloads altina indirildi!${NC}"
echo -e "${BLUE}===================================================${NC}"