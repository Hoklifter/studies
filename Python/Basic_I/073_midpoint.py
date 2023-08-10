#!/usr/bin/env python3


'''
73. Write a Python program to calculate the midpoints of a line.
'''

def midpoint(p1, p2):
    mid = [(p1[0] + p2[0])/2, (p1[1] + p2[1])/2]
    return tuple(mid)

X1y1 = 5, 4
x2y2 = 2, 6

print(midpoint(X1y1, x2y2))
