#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Updating system..."
pkg update -y

echo "[+] Installing system packages..."
pkg install -y \
    python \
    git \
    termux-api \
    clang \
    make

echo "[+] Installing pip..."
pip install --upgrade pip

echo "[+] Installing Python requirements..."
pip install -r requirements.txt

echo "[✓] Setup complete!"
