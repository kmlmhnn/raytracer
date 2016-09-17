#!/usr/bin/python
from __future__ import division
from vec3 import *
from ray import *
import math
import sys
import pdb
from hitable import *
from hitables import *
from sphere import *

def color(ray, world):
    hit_record = {}
    if world.hit(ray, 0.0, 1024.0, hit_record):
        return 0.5 * (hit_record['N'] + Vec3(1, 1, 1))
    else:
        ray_hat = hat(ray.direction)
        t = 0.5 * (ray_hat.y + 1.0)
        return (1.0 - t)*Vec3(1, 1, 1) + t*Vec3(0.5, 0.7, 1.0);


if __name__ == '__main__':
    width, height = 200, 100
    maxcolors = 255

    lower_left_corner = Vec3(-2, -1, -1) 
    horizontal = Vec3(4, 0, 0)
    vertical = Vec3(0, 2, 0)
    origin = Vec3(0, 0, 0)
    
    print "P3"
    print width, height
    print maxcolors

    world = Hitables([
        Sphere(Vec3(0, 0, -1), 0.5),
        Sphere(Vec3(0, -100.5, -1), 100)
    ])

    for y in range(height):
        for x in range(width):
            u, v = x / width, y / height
            ray = Ray(origin,
                    lower_left_corner + u*horizontal + v*vertical)
            col = color(ray, world) * maxcolors
            print int(col.x), int(col.y), int(col.z)





