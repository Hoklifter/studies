#!/usr/bin/env python3


'''
8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
'''


import re


def matches(text):
    pattern = r'[A-Z][a-z]+'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('Bacon'))

print(matches('bacon'))

print(matches('bAcon'))

print(matches('bacoN'))
