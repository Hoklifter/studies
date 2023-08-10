#!/usr/bin/env python3


'''
103. Write a Python program to extract the filename from a given path.
'''
import os.path
def filename(path):
    return os.path.basename(path)

print(filename('../source'))
