# Simpel3D-pi4gpu – GPU Treiber Basis
# von zoviloplay ( youtuber )

import os
import time

class GPUDriver:
    def __init__(self):
        self.memory = 256
        self.opengl = True
        self.fps_limit = 45
        self.running = False

    def load_config(self):
        print("Lade gpu.conf...")
        if os.path.exists("gpu.conf"):
            with open("gpu.conf", "r") as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split("=")
                        if key == "GPU_MEMORY":
                            self.memory = int(value)
                        if key == "FPS_LIMIT":
                            self.fps_limit = int(value)
            print("Konfiguration geladen:", self.memory, "MB, FPS:", self.fps_limit)
        else:
            print("gpu.conf nicht gefunden – Standardwerte werden benutzt.")

    def init_gpu(self):
        print("Initialisiere GPU...")
        os.system(f"sudo raspi-config nonint do_memory_split {self.memory}")
        print("GPU Speicher gesetzt:", self.memory, "MB")
        print("OpenGL ES aktiviert.")
        self.running = True

    def render_loop(self):
        print("Starte Render-Loop...")
        frame = 0
        while self.running and frame < 200:
            print("Render Frame:", frame)
            time.sleep(1 / self.fps_limit)
            frame += 1

    def shutdown(self):
        print("GPU-Treiber wird beendet...")
        self.running = False

if __name__ == "__main__":
    driver = GPUDriver()
    driver.load_config()
    driver.init_gpu()
    driver.render_loop()
    driver.shutdown()
