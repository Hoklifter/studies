#!/usr/bin/env python3


'''
3.Write a Python program that matches a string that has an a followed by one or more b's.
'''


import re


def matches(text):
    match_search = re.finditer(r'ab+', text)
    for match in match_search:
        if match:
            return 'Found.'
    return 'Not Found.'


print(matches('abobora'))
print(matches('avestruz'))
print(matches('marab'))
print(matches('morgob'))
print(matches('margob'))
