#!/usr/bin/env python3


'''
124. Write a Python program to check whether multiple variables have the same value.
'''

def all_equal(l : list):
    if len(set(l)) == 1:
        return f'{l} all values are equal.'
    return f'{l} all values are not equal'

a = b = c = 128
d = e = f = 256

print(all_equal([a, b, c]))
print(all_equal([a, e, c]))
print(all_equal([d, e, f]))
print(all_equal([e, a, b]))
