#!/usr/bin/env python3


'''
18. Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum.
'''


a = float(input('''Give the first number::
= '''))
b = float(input('''Give the second number::
= '''))
c = float(input('''Give the last number::
= '''))

if a == b == c:
    three_sum = (a + b + c)*3
    print(three_sum)
