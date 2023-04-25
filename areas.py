"""Defines the areas of different shapes"""

import math

def triangle(base, height):
    return base * height/2

def rectangle(length, width):
    return length * width

def circle(radius):
    return math.pi * (radius**2)

def doughnut(outside_radius, inside_radius):
    return circle(outside_radius) - circle(inside_radius)
