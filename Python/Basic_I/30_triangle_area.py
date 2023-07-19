#!/usr/bin/env python3


'''
30. Write a Python program that will accept the base and height of a triangle
and compute its area.
'''

b = float(input('''Type the base of the triangle:
= '''))
h = float(input('''Type the height of the triangle:
= '''))

A = b*h/2
print(f'The area of the triangle is {A}.')
