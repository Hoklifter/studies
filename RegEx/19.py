#!/usr/bin/env python3


'''
19. Write a Python program to search for literal strings within a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
'''


import re


def check(pattern, string):
    for x in re.finditer(pattern, string):
        if x:
            yield x
            continue
        else:
            return 'Not Found.'


pattern = r'fox|dog|horse'
string = 'The quick brown fox jumps over the lazy dog.'
gen = check(pattern, string)


for x in gen: print(x)
