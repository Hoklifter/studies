#!/usr/bin/env python3

import os, sys

__doc__ = f'''
49. Write a Python program to list all files in a directory.

Usage: python3 {os.path.basename(__file__)} <Directory>/<Directory path
'''

def files_in_dir(dirpath):
    return [x for x in os.listdir(dirpath) if os.path.isfile(x)]

sys.argv.append(os.path.dirname(__file__))
path = sys.argv[1]
dir_files = sorted(files_in_dir(path))
print('\t' + '\n\t'.join(dir_files))
