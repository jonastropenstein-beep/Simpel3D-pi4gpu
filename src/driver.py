# ============================================================
# pi4gpu – GPU Treiber + Simpel3D Engine Kopplung
# Entwickelt von (Zoviloplay – YouTube)
# ============================================================

import os
import time
from OpenGL.GL import *
from simpel3d import Simpel3D, Object3D

class GPUDriver:
    def __init__(self):
        # ------------------------------------------------------------
        # Grundkonfiguration des Treibers
        # ------------------------------------------------------------
        self.memory = 256
        self.opengl = True
        self.fps_limit = 45
        self.running = False

        # ------------------------------------------------------------
        # Interne Renderauflösung (720p)
        # GPU rendert IMMER in dieser Auflösung
        # Monitor bleibt groß (1440p/1900p)
        # ------------------------------------------------------------
        self.internal_width = 1280
        self.internal_height = 720

        # ------------------------------------------------------------
        # Ausgabeauflösung des Monitors
        # Wird später automatisch erkannt
        # ------------------------------------------------------------
        self.display_width = 2560
        self.display_height = 1440

        # ------------------------------------------------------------
        # Simpel3D Engine
        # ------------------------------------------------------------
        self.engine = Simpel3D()

    def load_config(self):
        # ------------------------------------------------------------
        # gpu.conf laden (Einstellungen des Treibers)
        # ------------------------------------------------------------
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

                        if key == "RENDER_WIDTH":
                            self.internal_width = int(value)

                        if key == "RENDER_HEIGHT":
                            self.internal_height = int(value)

            print(f"Konfiguration geladen: {self.memory}MB, FPS={self.fps_limit}, Render={self.internal_width}x{self.internal_height}")
        else:
            print("gpu.conf nicht gefunden – Standardwerte werden benutzt.")

    def init_gpu(self):
        # ------------------------------------------------------------
        # GPU initialisieren
        # Speicher setzen + OpenGL ES aktivieren
        # ------------------------------------------------------------
        print("Initialisiere GPU...")
        os.system(f"sudo raspi-config nonint do_memory_split {self.memory}")
        print("GPU Speicher gesetzt:", self.memory, "MB")
        print("OpenGL ES aktiviert.")
        self.running = True

        # ------------------------------------------------------------
        # Interner Framebuffer (720p)
        # Hier rendert Simpel3D hinein
        # ------------------------------------------------------------
        self.internal_fbo = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.internal_fbo)

        # interne Renderfläche
        self.internal_tex = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.internal_tex)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.internal_width, self.internal_height, 0, GL_RGB, GL_UNSIGNED_BYTE, None)

        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, self.internal_tex, 0)

        print(f"Interner Renderbuffer erstellt: {self.internal_width}x{self.internal_height}")

        # ------------------------------------------------------------
        # Testobjekt in Engine laden
        # ------------------------------------------------------------
        cube = Object3D()
        cube.move(1, 2, 3)
        cube.rotate(45, 0, 0)
        self.engine.add(cube)

    def render_loop(self):
        # ------------------------------------------------------------
        # Haupt-Renderloop
        # Engine → 720p → Upscaling → Monitor
        # ------------------------------------------------------------
        print("Starte Render-Loop...")
        frame = 0

        while self.running:
            # ------------------------------------------------------------
            # 1️⃣ INTERNES RENDERING (720p)
            # ------------------------------------------------------------
            glBindFramebuffer(GL_FRAMEBUFFER, self.internal_fbo)
            glViewport(0, 0, self.internal_width, self.internal_height)

            # Engine rendern
            self.engine.render()

            # ------------------------------------------------------------
            # 2️⃣ UPSCALING AUF MONITOR (z.B. 1440p)
            # ------------------------------------------------------------
            glBindFramebuffer(GL_READ_FRAMEBUFFER, self.internal_fbo)
            glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0)

            glBlitFramebuffer(
                0, 0, self.internal_width, self.internal_height,
                0, 0, self.display_width, self.display_height,
                GL_COLOR_BUFFER_BIT,
                GL_LINEAR
            )

            # ------------------------------------------------------------
            # FPS Limit
            # ------------------------------------------------------------
            time.sleep(1 / self.fps_limit)
            frame += 1

    def shutdown(self):
        # ------------------------------------------------------------
        # Treiber sauber beenden
        # ------------------------------------------------------------
        print("GPU-Treiber wird beendet...")
        self.running = False


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Startpunkt des Treibers
    # ------------------------------------------------------------
    driver = GPUDriver()
    driver.load_config()
    driver.init_gpu()
    driver.render_loop()
    driver.shutdown()
