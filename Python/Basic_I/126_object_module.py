#!/usr/bin/env python3


'''
126. Write a Python program to get the actual module object for a given object.
'''
from inspect import getmodule
from math import ceil
a = 'sample'
print(getmodule(a))
print(getmodule(ceil))
