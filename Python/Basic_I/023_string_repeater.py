#!/usr/bin/env python3


'''
23. Write a Python program to get n (non-negative integer) copies of the first 2
characters of a given string.
Return n copies of the whole string if the length is less than 2.
'''

n = 5
a = 'access'
b = 'zf'

def repeat(n, string):
    if len(string) > 2:
        return string[:2]*n
    return string * n

print(repeat(n, a))
print(repeat(n, b))
print(repeat(n, 'l'))
