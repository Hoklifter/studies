#!/usr/bin/env python3


'''
144. Write a Python program to check whether a variable is an integer or string.
'''

values = 'hiaehibdf', 72478245, (1, 2), 1.3434, [1, 2], {1, 2, 2}, {'a': 123, 'b' : 1234}

for val in values:
    print(f'value {val!r} is {type(val).__name__}')
