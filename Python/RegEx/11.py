#!/usr/bin/env python3


'''
11. Write a Python program that matches a word at the end of a string, with optional punctuation.
'''


import re


def matches(text):
    pattern = r'string[.!?]*$'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'



print(matches('random string.'))

print(matches('random string?'))

print(matches('random string!'))

print(matches('random string'))

print(matches('string random'))
