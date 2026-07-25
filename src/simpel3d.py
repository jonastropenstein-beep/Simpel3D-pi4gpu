# Simpel3D – Basis 3D Engine
# von Jonas (zoviloplay)

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

class Renderer:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def render(self):
        print("Rendering Szene...")
        for obj in self.objects:
            print(f"Objekt @ Pos({obj.position.x}, {obj.position.y}, {obj.position.z}) "
                  f"Rot({obj.rotation.x}, {obj.rotation.y}, {obj.rotation.z})")

if __name__ == "__main__":
    renderer = Renderer()

    cube = Object3D()
    cube.move(1, 2, 3)
    cube.rotate(45, 0, 0)

    renderer.add(cube)
    renderer.render()
