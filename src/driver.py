# ============================================================
# pi4gpu – GPU Treiber + Simpel3D Engine Kopplung
# Entwickelt von (Zoviloplay – YouTube)
# Effekte deaktiviert: GPU zeichnet nur rohe Objekte
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
        # ------------------------------------------------------------
        self.internal_width = 1280
        self.internal_height = 720

        # ------------------------------------------------------------
        # Ausgabeauflösung des Monitors
        # ------------------------------------------------------------
        self.display_width = 2560
        self.display_height = 1440

        # ------------------------------------------------------------
        # Simpel3D Engine
        # ------------------------------------------------------------
        self.engine = Simpel3D()

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

                        if key == "RENDER_WIDTH":
                            self.internal_width = int(value)

                        if key == "RENDER_HEIGHT":
                            self.internal_height = int(value)

            print(f"Konfiguration geladen: {self.memory}MB, FPS={self.fps_limit}, Render={self.internal_width}x{self.internal_height}")
        else:
            print("gpu.conf nicht gefunden – Standardwerte werden benutzt.")

    def init_gpu(self):
        print("Initialisiere GPU...")
        os.system(f"sudo raspi-config nonint do_memory_split {self.memory}")
        print("GPU Speicher gesetzt:", self.memory, "MB")
        print("OpenGL ES aktiviert.")
        self.running = True

        # ------------------------------------------------------------
        # Effekte deaktivieren (maximale Performance)
        # ------------------------------------------------------------
        glDisable(GL_LIGHTING)
        glDisable(GL_FOG)
        glDisable(GL_BLEND)
        glDisable(GL_DITHER)
        glDisable(GL_MULTISAMPLE)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)

        print("Alle GPU-Effekte deaktiviert – Rohmodus aktiv.")

        # ------------------------------------------------------------
        # Interner Framebuffer (720p)
        # ------------------------------------------------------------
        self.internal_fbo = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.internal_fbo)

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
        print("Starte Render-Loop...")
        frame = 0

        while self.running:
            # ------------------------------------------------------------
            # 1️⃣ INTERNES RENDERING (720p)
            # ------------------------------------------------------------
            glBindFramebuffer(GL_FRAMEBUFFER, self.internal_fbo)
            glViewport(0, 0, self.internal_width, self.internal_height)

            # Engine rendern (ohne Effekte)
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
        print("GPU-Treiber wird beendet...")
        self.running = False


if __name__ == "__main__":
    driver = GPUDriver()
    driver.load_config()
    driver.init_gpu()
    driver.render_loop()
    driver.shutdown()
