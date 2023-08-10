#!/usr/bin/env python3


'''
33. Write a Python program to sum three given integers. However, if two values
are equal, the sum will be zero.
'''

def sum_integers(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    return sum([a, b, c])

print(sum_integers(1, 2 ,3))
print(sum_integers(1, 1 ,3))
