#!/usr/bin/env python3


'''
36. Write a Python program to add two objects if both objects are integers.
'''

def add_int(a, b):
    if all([isinstance(a, int), isinstance(b, int)]):
        return a + b
    return 'Non-integer value provided'

print(add_int(1, 2))
print(add_int(10, 20))
print(add_int('a', 2))
print(add_int('a', 'b'))
print(add_int(1.0, 20))
print(add_int(10.5, 20))
