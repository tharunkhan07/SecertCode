#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "[+] Updating Termux..."
pkg update -y

echo "[+] Installing system packages..."
pkg install -y \
  python \
  git \
  termux-api \
  clang \
  make

echo "[+] Upgrading pip..."
python -m ensurepip
pip install --upgrade pip

echo "[+] Installing Python requirements..."
pip install -r requirements.txt

echo "[✓] Setup completed successfully!"


