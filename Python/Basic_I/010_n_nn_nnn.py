#!/usr/bin/env python3


'''
10. Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

int_input = input('''Type an integer.
= ''')
result = 0
for x in range(1, 3+1):
    result += int(int_input * x)
print(f'{result = }')
