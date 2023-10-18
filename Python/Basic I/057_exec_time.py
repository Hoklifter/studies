#!/usr/bin/env python3


'''
57. Write a Python program to get the execution time of a Python method.
'''

import time

def display():
    print('Foo')
    print('Bar')

start = time.time()
display()
end = time.time()
print(f'Execution time of the "display()" method :\n {end - start}')
