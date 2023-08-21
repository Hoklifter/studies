#!/usr/bin/env python3


'''
113. Write a Python program that inputs a number and
generates an error message if it is not a number.
'''
try:
    n = int(input('Enter a number.\n = '))
except ValueError:
    raise ValueError('Incorrect Input: Only numbers will be accepted')
