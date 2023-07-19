#!/usr/bin/env python3


'''
7. Write a Python program to find sequences of lowercase letters joined by an underscore.
'''


import re


def matches(text):
    pattern = r'[a-z]+_[a-z]+'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('bacon_frito'))
print(matches('bacon frito'))
print(matches('bacon_cru'))
print(matches('bacon cru'))
print(matches('bacon_cozido'))
print(matches('bacon cozido'))
