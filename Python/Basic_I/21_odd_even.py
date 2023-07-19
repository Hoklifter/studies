#!/usr/bin/env python3


'''
21. Write a Python program that determines whether a given number
(accepted from the user) is even or odd, and prints an
appropriate message to the user.
'''

n = int(input('''Provide a number:
= '''))
if n:
    if n % 2 == 0:
        print(f'The number {n} is even.')
    else:
        print(f'The number {n} is odd')
