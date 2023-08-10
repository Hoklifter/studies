#!/usr/bin/env python3


'''
60. Write a Python program to calculate the hypotenuse of a right angled
triangle.
'''


def hypotenuse(a, b):

    from math import sqrt

    a, b = float(a), float(b)
    if all([a > 0, b > 0]):
        return sqrt(a**2 + b**2)
    return


u_a = input('\tPass a side of the triangle.\n = ')
u_b = input('\tPass the other side of the triangle.\n = ')
print(f'The hypotenuse of the triangle is {hypotenuse(u_a, u_b)}.')
