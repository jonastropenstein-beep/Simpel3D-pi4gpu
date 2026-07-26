#!/bin/bash
# Simpel3D-pi4gpu Install Script

echo "Installiere Simpel3D-pi4gpu..."

# Ordner erstellen
sudo mkdir -p /opt/simpel3d-pi4gpu

# Dateien aus dem App-Ordner kopieren
sudo cp -r "$APPDIR/src" /opt/simpel3d-pi4gpu/
sudo cp "$APPDIR/icon.png" /opt/simpel3d-pi4gpu/

# Startbefehl verlinken
sudo ln -sf /opt/simpel3d-pi4gpu/src/main.py /usr/local/bin/simpel3d-pi4gpu

# Desktop-Verknüpfung erstellen
DESKTOP_FILE="$HOME/Desktop/Simpel3D-pi4gpu.desktop"

echo "[Desktop Entry]" > "$DESKTOP_FILE"
echo "Name=Simpel3D-pi4gpu" >> "$DESKTOP_FILE"
echo "Exec=simpel3d-pi4gpu" >> "$DESKTOP_FILE"
echo "Icon=/opt/simpel3d-pi4gpu/icon.png" >> "$DESKTOP_FILE"
echo "Type=Application" >> "$DESKTOP_FILE"

chmod +x "$DESKTOP_FILE"

echo "Installation abgeschlossen!"
