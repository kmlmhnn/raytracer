#!/usr/bin/python
from __future__ import division
from vec3 import *

if __name__ == '__main__':
    width, height = 200, 100
    maxcolors = 255
    
    print "P3"
    print width, height
    print maxcolors

    for y in range(height):
        for x in range(width):
            color = Vec3(x / width, y / height, 0.2)
            color *= maxcolors
            print int(color.x), int(color.y), int(color.z)




