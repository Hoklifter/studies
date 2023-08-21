#!/usr/bin/env python3


'''
130. Write a Python program that uses double quotes to display strings.
'''

strings = 'afafa', 'jsfiusuf', 'jsodfsf'
for string in strings:
    print(f'''{repr(string).replace("'", '"')}''')
