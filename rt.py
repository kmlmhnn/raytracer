#!/usr/bin/python
from __future__ import division
from vec3 import *
from ray import *
import pdb

def color(ray):
    ray_hat = hat(ray.direction)
    t = 0.5 * (ray_hat.y + 1.0)
    return (1 - t) * Vec3(1, 1, 1) + t * Vec3(0.5, 0.7, 1.0)

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

    for y in range(height):
        for x in range(width):
            u, v = x / width, y / height
            ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical)
            col = color(ray) * maxcolors
            print int(col.x), int(col.y), int(col.z)





