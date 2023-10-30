#!/usr/bin/env python3


'''
129. Write a Python program to add leading zeroes to a string.
'''


strings = '1234', '123', '12', '1'

for string in strings:
    while len(string) < 4:
        string = f'0{string}'
    print(string)
