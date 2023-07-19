#!/usr/bin/env python3


'''
13. Write a Python program that matches a word containing 'z', not the start or end of the word.
'''


import re


def matches(text):
    pattern = r'[a-zA-Z]+z[a-zA-Z]+'
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
