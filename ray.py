from vec3 import *

class Ray:
    def __init__(self, a=Vec3(0, 0, 0), b=Vec3(1, 0, 0)):
        self.origin = a
        self.direction = b

    def getpoint(self, t):
        return self.origin + t * self.direction

