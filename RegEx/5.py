#!/usr/bin/env python3


'''
5. Write a Python program that matches a string that has an a followed by three 'b'.
'''


import re


def matches(text):
    match_find = re.finditer('ab{3}', text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('abb'))
print(matches('ab'))
print(matches('abbb'))
print(matches('dab'))
print(matches('dabb'))
