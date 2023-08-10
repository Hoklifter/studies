#!/usr/bin/env python3


'''
93. Write a Python program to get the Identity, Type, and Value of an object.
'''

obj = 'adajn'
obj_identity = id(obj)
obj_type = type(obj).__name__

print(f'{obj_identity = }\n{obj_type = }\nobj_value = {obj}')
