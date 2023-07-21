#!/usr/bin/env python3


'''
41. Write a Python program to check whether a file exists.
'''

from os.path import exists, basename, isfile
from sys import argv

def file_exist(filepath):
    return exists(filepath) and isfile(filepath)

if len(argv) > 1:
    filepath = argv[1]
    if file_exist(filepath):
        print(f'The file "{basename(filepath)}" exists.')
    else:
        print(f'File not found.')
else:
    print(f'Usage: python3 {basename(__file__)} <File>/<Filepath>')
