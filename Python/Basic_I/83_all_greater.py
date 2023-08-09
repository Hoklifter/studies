#!/usr/bin/env python3


'''
83. Write a Python program to test whether all numbers in a list are greater
than a certain number.
'''

lists = [1, 2, 3], [5, 6, 7], [4, 5, 6], [9, 8, 10]
certain_number = 4
for x in lists:
    print(min(x) > certain_number)
