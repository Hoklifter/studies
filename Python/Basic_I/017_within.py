#!/usr/bin/env python3


'''
17.
Write a Python program to test whether a number is within 100 of 1000
or 2000
'''
n = int(input('''Give a number:
= '''))

if n in range(1000, 1101):
    print(f"The number {n} is within 100 of 1000.")
elif n in range(2000, 2101):
    print(f"The number {n} is within 100 of 2000.")
else:
    print(f"The number {n} is not within 100 of 1000 or 2000.")
