#!/usr/bin/env python3


'''
121. Write a Python program to determine if a variable is defined or not.
'''
defined_var = 'a'
try:
    print(f'{defined_var = }')
    print(f'{undefined_var = }')
except NameError:
    print('Variable is not defined.')
