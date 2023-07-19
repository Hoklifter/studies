#!/usr/bin/env python3


'''
17. Write a Python program to check for a number at the end of a string.
'''


import re


def check(pattern, string):
    for x in re.finditer(pattern, string):
        return 'Found!'
    return 'Not Found.'

strings = ['a1', 'a1b', '1ab', 'ab1 1ab', '1ab ba1']
for x in strings:
    print(check(r'1$', x))
