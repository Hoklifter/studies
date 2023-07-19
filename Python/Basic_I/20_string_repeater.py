#!/usr/bin/env python3


'''
20. Write a Python program that returns a string that is n
(non-negative integer) copies of a given string.
'''
string = input('''Give a string:
\t''')
if string:
    n = abs(int(input('''How many times you want to repeat the string?
    \t''')))

    print(string * n)
