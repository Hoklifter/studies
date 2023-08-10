#!/usr/bin/env python3


'''
5. Write a Python program that accepts the user's first and last name and
prints them in reverse order with a space between them.
'''

user_name = input('''Whats your first and last name?
= ''').split()
try:
    first_name = user_name[0]
    last_name = user_name[1]
    print(last_name, first_name)
except (IndexError, NameError):
    print('Provide a valid name (Ex. Marcus Pelotas).')
