from __future__ import division
import abc
from hitable import Hitable
from vec3 import *
import math

class Sphere(Hitable):
    def __init__(self, center=Vec3(0, 0, 0), radius=1.0):
        self.center = center
        self.radius = float(radius)
    
    def hit(self, ray, t_min, t_max, hit_record):
        oc = ray.origin - self.center
        a = dot(ray.direction, ray.direction)
        b = dot(oc, ray.direction)
        c = dot(oc, oc) - self.radius*self.radius
        delta = b*b - a*c
        
        if delta > 0:
            temp = (-b - math.sqrt(b*b - a*c)) / a
            if temp < t_max and temp > t_min:
                hit_record['t'] = temp
                hit_record['p'] = ray.getpoint(temp)
                hit_record['N'] = (hit_record['p'] - self.center) / self.radius
                return True
            temp = (-b + math.sqrt(b*b - a*c)) / a
            if temp < t_max and temp > t_min:
                hit_record['t'] = temp
                hit_record['p'] = ray.getpoint(temp)
                hit_record['N'] = (hit_record['p'] - self.center) / self.radius
                return True

        else:
            return False




 






