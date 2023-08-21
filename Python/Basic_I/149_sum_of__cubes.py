#!/usr/bin/env python3


'''
149. Write a Python function that takes a positive integer and returns the sum
of the cube of all positive integers smaller than the specified number.
'''

def sum_of_cubes_series(n):
    sum_cubes = 0
    for x in range(n): sum_cubes += x**3
    return sum_cubes

positive_integer = abs(int(input('''Enter a number and the program will return the
sum of the cubes of all positive numbers before it.\n = ''')))
result = sum_of_cubes_series(positive_integer)
print(f'the sum of the cubes of all positive numbers before {positive_integer} is {result}')
