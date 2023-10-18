#!/usr/bin/env python3


'''
141. Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04
'''

sample = 30, 4

for x in sample:
    print(f'{x:02x}')
