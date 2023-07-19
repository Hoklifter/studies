#!/usr/bin/env python3


'''
9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
'''


import re


def matches(text):
    pattern = r'a.+b$'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('abakub'))

print(matches('abaku'))

print(matches('bukaba'))

print(matches('kabuab'))

print(matches('ab'))
