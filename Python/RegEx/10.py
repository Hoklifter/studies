#!/usr/bin/env python3


'''
10. Write a Python program that matches a word at the beginning of a string.
'''



import re


def matches(text):
    pattern = r'^random'
    match_find = re.finditer(pattern, text)
    for match in match_find:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('random'))

print(matches('random string'))

print(matches('string random'))

print(matches('randomim'))

print(matches('testerandom'))
