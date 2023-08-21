#!/usr/bin/env python3


'''
114. Write a Python program to filter positive numbers from a list.
'''

import random

l = []
while len(l) < 10:
    l.append(random.randint(-3000, 3000))

print(l)
print(f'Only positive numbers : {[x for x in l if x >= 0]}')
