#!/usr/bin/env python3


'''
108. Write a Python program to find the path to a file or directory
when you encounter a path name.
'''

import os.path

paths = [
    __file__,
    os.path.dirname(__file__),
    '/',
    './broken_link'
]

for path in paths:
    print(f'File          :  {path}')
    print(f'Absolute      :  {os.path.isabs(path)}')
    print(f'Is File?      :  {os.path.isfile(path)}')
    print(f'Is Dir?       :  {os.path.isdir(path)}')
    print(f'Is Link?      :  {os.path.islink(path)}')
    print(f'Exists?       :  {os.path.exists(path)}')
    print(f'Link Exists?  :  {os.path.lexists(path)}\n')
