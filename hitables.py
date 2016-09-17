import abc
from hitable import Hitable
from vec3 import *
import math

class Hitables(Hitable):
    def __init__(self, l=[]):
        self.items = l

    def hit(self, ray, t_min ,t_max, hit_record):
        temp_record = {}
        hit_anything = False
        closest_so_far = t_max

        for item in self.items:
            if item.hit(ray, t_min, closest_so_far, temp_record):
                hit_anything = True
                closest_so_far = temp_record['t']
                for key in temp_record:
                    hit_record[key] = temp_record[key]

        return hit_anything




