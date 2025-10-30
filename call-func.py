#! /usr/bin/env python3
import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10))

def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs2(20))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'No real roots'
    elif d == 0:
        x = -b / (2 * a)
        return x,
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2