#!/bin/bash
echo "Deinstalliere Simpel3D-pi4gpu..."

sudo rm -rf /opt/simpel3d-pi4gpu
sudo rm -f /usr/local/bin/simpel3d-pi4gpu
rm -f ~/Desktop/Simpel3D-pi4gpu.desktop

echo "Simpel3D-pi4gpu wurde erfolgreich entfernt."
