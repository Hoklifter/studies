#!/usr/bin/env python3


'''
26. Write a Python program to create a histogram from a given list of integers.
'''

integers = [2, 5, 1, 6, 7]
histogram = ''
for x in integers:
    histogram += f'{"|"*x}\n'

print(histogram)
