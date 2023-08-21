#!/usr/bin/env python3


'''
131. Write a Python program to split a variable length string into variables.
'''

string = 'Kauã, Brazilian, 18'
name, nationality, age = string.split(', ')
print(f'{string = }\n{name = }\n{nationality = }\n{age = }')
