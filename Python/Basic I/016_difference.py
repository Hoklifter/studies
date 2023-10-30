#!/usr/bin/env python3


'''
16. Write a Python program to calculate the difference between a given number
and 17. If the number is greater than 17, return twice the absolute difference.
'''

x = float(input('''Give a number.
= '''))
to_compare = 17
difference = x-to_compare
print(f'Difference between {x} and {to_compare} is {difference}.')
if x > to_compare:
    difference = abs(difference)*2
    print(f'Twice the absolute difference is {difference}.')
