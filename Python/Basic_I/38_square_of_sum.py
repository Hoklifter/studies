#!/usr/bin/env python3


'''
38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''

def square_of_sum(x, y):
    return (x + y) ** 2

x = 4
y = 3
result = square_of_sum(x, y)

print(f'Output : ({x} + {y}) ^ 2) = {result}')
