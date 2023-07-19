#!/usr/bin/env python3


'''
4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
'''


import re


def matches(text):
    match_find = re.finditer('ab?', text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('abb'))
print(matches('ab'))
print(matches('abc'))
print(matches('dab'))
print(matches('dabb'))
