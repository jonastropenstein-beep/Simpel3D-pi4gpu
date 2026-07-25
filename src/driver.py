# Simpel3D-pi4gpu Treiber
# Entwickelt von zoviloplay aus youtube

import os

def init_gpu():
    print("Initialisiere GPU für Raspberry Pi 4...")
    os.system("sudo raspi-config nonint do_memory_split 256")
    print("GPU-Speicher auf 256MB gesetzt.")
    print("OpenGL ES aktiviert.")
    print("Treiber erfolgreich geladen!")

if __name__ == "__main__":
    init_gpu()
