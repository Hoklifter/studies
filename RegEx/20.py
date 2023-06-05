#!/usr/bin/env python3


'''
20.
Write a Python program to search for a literal string in a string and
also find the location within the original string where the pattern occurs.
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


for x in gen:
    print(f"""Match '{x.group()}' at index {x.span()[0]}""")
