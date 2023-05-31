#!/usr/bin/env python3
'''
11. Write a Python program to find the intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
'''

A1 = [1, 2, 3, 5, 7, 8, 9, 10]
A2 = [1, 2, 4, 8, 9]
intersections = lambda a, b : [x for x in a if x in b]
A3 = intersections(A1, A2)
print(f'''Original arrays:
{A1}
{A2}
Intersection of the said arrays: {A3}''')
