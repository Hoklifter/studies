#!/usr/bin/env python3


'''
128. Write a Python program to check whether lowercase letters exist in a string.
'''

def lowercases_in_string(s):
    lowercase__chars = [x for x in s if x.islower()]
    return lowercase__chars

strings = 'sdfjsofsoJAHFUAFAFA','ADHBFDAFDAHBSFB', '@UH$(@@', 'ksf#*#)', ' '

for string in strings:
    lowercase_chars = lowercases_in_string(string)
    if lowercase_chars:
        print(f'''
The string {string!r} have lowercase characters:
\t{lowercase_chars}
''')
    else:
        print(f'''
The string {string!r} does not have lowercase characters.
''')
