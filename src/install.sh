#!/bin/bash
echo "Starte Installation von Simpel3D-pi4gpu..."
sudo apt update
sudo apt install -y python3
echo "Kopiere GPU-Konfiguration..."
sudo cp gpu.conf /etc/simpel3d.conf
echo "Starte Treiber..."
python3 driver.py
echo "Installation abgeschlossen!"
