#!/usr/bin/env python3


'''
40. Write a Python program to calculate the distance between the points (x1, y1)
and (x2, y2).
'''

from math import sqrt

def distance(p, q):
    x1, y1 = p
    x2, y2 = q
    d = sqrt(
        (x2 - x1)**2 + (y2 - y1)**2
    )

    return d

print(
    distance(
        (1, 2),
        (3, 4)
    )
)
