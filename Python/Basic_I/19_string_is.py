#!/usr/bin/env python3


'''
19. Write a Python program to get a newly-generated string from a given string
where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".
'''

given = input('''Give a string:
= ''')

if given[:2] != 'Is':
    given = 'Is ' + given

print(given)
