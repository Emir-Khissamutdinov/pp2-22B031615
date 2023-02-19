import math


def radians(degrees):
    return degrees / 360 * 2 * math.pi


def trapezoid_area(height, base1, base2):
    return (base1 + base2) / 2 * height


def polygon_area(sides, length):
    return (sides * length) / (4 * math.tan(math.pi / sides))


def parallelogram_area(base, height):
    return base * height
