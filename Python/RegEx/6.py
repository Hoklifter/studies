#!/usr/bin/env python3


'''
6. Write a Python program that matches a string that has an a followed by two to three 'b'.
'''


import re


def matches(text):
    match_find = re.finditer(r'ab{2,3}', text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('abb'))
print(matches('ab'))
print(matches('abbb'))
print(matches('dabbbb'))
print(matches('dabb'))
