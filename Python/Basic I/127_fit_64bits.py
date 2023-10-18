#!/usr/bin/env python3


'''
127. Write a Python program to check whether an integer fits in 64 bits.
'''

def fit_64bits(n):
    return n.bit_length() < 64

nums = 2 ** 70, 2**60

for x in nums:
    if fit_64bits(x):
        print(f'The number {x} fit in 64 bits.')
    else:
        print(f'The number {x} does not fit in 64 bits.')
