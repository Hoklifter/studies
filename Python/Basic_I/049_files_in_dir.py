#!/usr/bin/env python3


'''
49. Write a Python program to list all files in a directory.
'''

import os, sys

def files_in_dir(dirpath):
    return list(filter(lambda f : os.path.isfile(f), os.listdir(dirpath)))

if len(sys.argv) > 1:
    path = sys.argv[1]
    dir_files = sorted(files_in_dir(path))
    if dir_files:
        print('\t' + '\n\t'.join(dir_files))
    else:
        print('\tNo files found.')
else:
    print(
f'Usage: python3 {os.path.basename(__file__)} <Directory>/<Directory path'
    )
