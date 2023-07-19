#!/usr/bin/env python3


'''
15. Write a Python program that starts each string with a specific number.
'''


import re


def matches(text):
    pattern = r'^1'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        # print(match)
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('1z'))

print(matches('a aza'))

print(matches('1muzician'))

print(matches(' 1mozart'))

print(matches('1mumz'))

print(matches('1mumo'))
