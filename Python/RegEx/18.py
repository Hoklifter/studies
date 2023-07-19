#!/usr/bin/env python3


'''
18. Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.

"Exercises number 1, 12, 13, and 345 are important"
'''


import re


def check(pattern, string):
    for x in re.finditer(pattern, string):
        if x:
            yield x
            continue
        else:
            return 'Not Found.'


pattern = r'[0-9]{1,3}'
string = "Exercises number 1, 12, 13, and 345 are important"
gen = check(pattern, string)


for x in gen: print(x)
