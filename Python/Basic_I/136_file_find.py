#!/usr/bin/env python3


'''
136. Write a Python program to
find files and skip directories in a given directory.

This just calls 049_files_in_dir.py, and cannot receive arguments.
'''

from subprocess import call
from sys import argv
call(['python3', '049_files_in_dir.py'])
