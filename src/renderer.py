#!/usr/bin/env python3
# Simpel3D-pi4gpu – 3D Renderer
# Autor: zoviloplay

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time

# Würfel-Koordinaten
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,7),
    (7,6),
    (6,4),
    (0,4),
    (1,5),
    (2,7),
    (3,6)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def start_renderer():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    rotation = 0

    print("[INFO] Renderer gestartet (720p, OpenGL)")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("[INFO] Renderer beendet.")
                return

        rotation += 1
        glRotatef(1, 3, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    start_renderer()
