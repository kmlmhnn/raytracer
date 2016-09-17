from __future__ import division
import math

class Vec3(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __repr__(self):
        return str((self.x, self.y, self.z))

    def __pos__(self):
        return self

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __abs__(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, other):
        try:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        except:
            self.x *= other
            self.y *= other
            self.z *= other
        return self

    def __itruediv__(self, other):
        try:
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        except:
            self.x /= other
            self.y /= other
            self.z /= other
        return self

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        try:
            return Vec3(self.x * other, self.y * other, self.z * other)
        except:
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            return Vec3(self.x / other, self.y / other, self.z / other)
        except:
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

def dot(a, b):
    return a.x*b.x + a.y*b.y +a.z*b.z

def cross(a, b):
    return Vec3(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x)

def hat(a):
    return a / abs(a)


    



