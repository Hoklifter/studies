#!/usr/bin/env python3
'''
7. Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False
'''
strings = ['abc', 'bca']
check_start_a = lambda string : True if string[0] == 'a' else False
for string in strings: print(check_start_a(string))
