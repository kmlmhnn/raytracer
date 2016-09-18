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
from camera import *
from random import random, seed

def random_vector():
    p = 2.0 * Vec3(random(), random(), random()) - Vec3(1, 1, 1)
    while dot(p, p) >= 1.0:
        p = 2.0 * Vec3(random(), random(), random()) - Vec3(1, 1, 1)
    return p


def color(ray, world):
    hit_record = {}
    if world.hit(ray, 0.0, 1024.0, hit_record):
        target = hit_record['p'] + hit_record['N'] + random_vector()
        return 0.5*color(Ray(hit_record['p'], target-hit_record['p']),
            world)
    else:
        ray_hat = hat(ray.direction)
        t = 0.5 * (ray_hat.y + 1.0)
        return (1.0 - t)*Vec3(1, 1, 1) + t*Vec3(0.5, 0.7, 1.0);


if __name__ == '__main__':
    width, height = 200, 100
    maxcolors = 255
    samples = 25   # set it to 100 for high quality images
    seed()

    print "P3"
    print width, height
    print maxcolors

    world = Hitables([
        Sphere(Vec3(0, 0, -1), 0.5),
        Sphere(Vec3(0, -100.5, -1), 100)
    ])

    camera = Camera()

    for y in range(height-1, 0, -1):
        for x in range(width):
            # u, v = x / width, y / height
            # ray = Ray(origin,
                    # lower_left_corner + u*horizontal + v*vertical)
            # col = color(ray, world) * maxcolors
            col = Vec3(0, 0, 0)
            for s in range(samples):
                u = (x + random()) / width
                v = (y + random()) / height
                ray = camera.getray(u, v)
                col += color(ray, world)
            col = col * maxcolors / samples
            print int(col.x), int(col.y), int(col.z)





