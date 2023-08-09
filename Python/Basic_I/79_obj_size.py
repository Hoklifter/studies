#!/usr/bin/env python3


'''
79. Write a Python program to get the size of an object in bytes.
'''
import sys

objects = 1134414, '2423489', 1244342.0, True

for x in objects:
    print(f'{x!r} size = {sys.getsizeof(x)} b')
