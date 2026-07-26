#!/usr/bin/env python3
# Simpel3D-pi4gpu – Hauptprogramm
# Autor: zoviloplay

import time
import gpu
import renderer

def main():
    print("=== Simpel3D-pi4gpu gestartet ===")

    # GPU-Setup
    print("[STEP] GPU-Konfiguration wird ausgeführt...")
    gpu.check_gpu_info()
    gpu.set_resolution()
    gpu.optimize_gpu()

    print("[OK] GPU ist bereit!")
    time.sleep(1)

    # Renderer starten
    print("[STEP] Starte Renderer...")
    renderer.start_renderer()

    print("[DONE] Simpel3D-pi4gpu wurde beendet.")

if __name__ == "__main__":
    main()
