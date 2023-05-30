#!/usr/bin/env python3
'''
9. Write a Python program to check whether a given string is a number or not using Lambda.
Sample Output:
True
True
False
True
False
True
'''
strings = ['-123', '12', 'a2', '123124', 'sdf3', '1343']
check = lambda string : True if string.replace('-', '').replace('.', '').isnumeric() else False
for x in strings: print(check(x))
