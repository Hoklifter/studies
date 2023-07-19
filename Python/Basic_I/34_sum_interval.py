#!/usr/bin/env python3


'''
34. Write a Python program to sum two given integers. However, if the sum is
between 15 and 20 it will return 20.
'''

def sum_integers(a, b):
    result = a + b
    if result > 15 < 20:
        return 20
    return result

print(sum_integers(2, 9))
print(sum_integers(14, 2))
print(sum_integers(18, 1))
print(sum_integers(19, 0))
