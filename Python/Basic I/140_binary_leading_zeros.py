#!/usr/bin/env python3


'''
140. Write a Python program to convert an integer to binary that keeps leading zeros.
Sample data : x=12
Expected output : 00001100
0000001100
'''
x = 12
print(f'{x:08b}\n{x:010b}')
