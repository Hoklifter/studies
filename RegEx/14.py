#!/usr/bin/env python3


'''
14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores. '''


import re


def matches(text):
    pattern = r'^\w+$'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        # print(match)
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('z'))

print(matches('a aza'))

print(matches('muzician'))

print(matches('mozart'))

print(matches('mumz'))

print(matches('mumo'))
