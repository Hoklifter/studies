#!/usr/bin/env python3


'''
132. Write a Python program to list the home directory without an absolute path.
'''
import os

print(sorted(os.listdir(os.path.expanduser('~'))))
