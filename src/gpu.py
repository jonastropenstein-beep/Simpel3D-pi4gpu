#!/usr/bin/env python3
# Simpel3D-pi4gpu – GPU-Management für Raspberry Pi 4
# Autor: zoviloplay

import os
import subprocess

def check_gpu_info():
    """Liest GPU-Informationen aus und gibt sie zurück."""
    try:
        gpu_info = subprocess.check_output(["vcgencmd", "get_mem", "gpu"]).decode().strip()
        print(f"[INFO] GPU-Speicher: {gpu_info}")
    except Exception as e:
        print(f"[WARN] GPU-Info konnte nicht gelesen werden: {e}")

def set_resolution(width=1280, height=720):
    """Setzt die Bildschirmauflösung auf 720p."""
    try:
        os.system(f"xrandr --output HDMI-1 --mode {width}x{height}")
        print(f"[INFO] Auflösung gesetzt auf {width}x{height}")
    except Exception as e:
        print(f"[ERROR] Konnte Auflösung nicht setzen: {e}")

def optimize_gpu():
    """Aktiviert GPU-Optimierungen für bessere 3D-Leistung."""
    print("[INFO] Aktiviere GPU-Optimierungen...")
    os.system("sudo raspi-config nonint do_memory_split 256")
    os.system("sudo raspi-config nonint do_overclock arm_freq 1800")
    print("[INFO] GPU-Optimierung abgeschlossen.")

def main():
    print("=== Simpel3D-pi4gpu ===")
    check_gpu_info()
    set_resolution()
    optimize_gpu()
    print("[DONE] GPU-Konfiguration abgeschlossen.")

if __name__ == "__main__":
    main()
