#!/usr/bin/env python3


'''
7. Write a Python program that accepts a filename from the user and prints
the extension of the file.
Sample filename : abc.java
Output : java
'''
import sys

doc = """Returns the extension of a file. (Ex. abc.java -> java).
Usage: python3 7_file_extension.py <filename>"""

def file_extension(filename):
    'Returns the extension of a file. (Ex. abc.java -> java)'
    filename = filename.split('.', maxsplit=1)
    if len(filename) == 2:
        return f'.{filename[1]}'
    return

if len(sys.argv) != 2:
    print (doc)
else:
    filename = sys.argv[1]
    extension = file_extension(filename)
    print(f'''The file {filename} has a {extension} extension''')
