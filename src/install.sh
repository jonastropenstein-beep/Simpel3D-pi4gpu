#!/bin/bash
# Simpel3D-pi4gpu Installer
# von Zoviloplay (YouTube)

echo "Installiere Simpel3D-pi4gpu..."
sudo apt update
sudo apt install -y python3 python3-pip python3-opengl
git clone https://github.com/jonastropenstein-beep/Simpel3D-pi4gpu.git
cd Simpel3D-pi4gpu/src
echo "Installation abgeschlossen!"
