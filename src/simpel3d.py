# Simpel3D – Mini 3D Engine für pi4gpu
# von zoviloplay (youtuber)

from OpenGL.GL import *
import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class Object3D:
    def __init__(self):
        self.position = Vector3()
        self.rotation = Vector3()
        self.scale = Vector3(1, 1, 1)

    def move(self, x, y, z):
        self.position.x += x
        self.position.y += y
        self.position.z += z

    def rotate(self, x, y, z):
        self.rotation.x += x
        self.rotation.y += y
        self.rotation.z += z

class Simpel3D:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def render(self):
        # Hier wird später echtes Rendering stehen
        glClearColor(0.1, 0.1, 0.1, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        # Debug-Ausgabe
        for obj in self.objects:
            print(f"Render Objekt: Pos({obj.position.x}, {obj.position.y}, {obj.position.z}) "
                  f"Rot({obj.rotation.x}, {obj.rotation.y}, {obj.rotation.z})")
