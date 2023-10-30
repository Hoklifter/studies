#!/usr/bin/env python3


'''
117. Write a Python program to prove that two string variables of the same
value point to the same memory location.
'''
string1 = string2 = 'abc'

print(f'{id(string1)} {id(string2)}')
print(f'string1 : {hex(id(string1))}\nstring2 : {hex(id(string2))}')
print(f'Share same location? : {id(string1) == id(string2)}')
