#!/usr/bin/env python3


'''
68. Write a Python program to calculate sum of digits of a number.
'''
num = 12345
sum_of_digits = sum([int(x) for x in str(num)])
print(f'\nThe sum of digits of {num} is {sum_of_digits}.')
