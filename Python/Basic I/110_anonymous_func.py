#!/usr/bin/env python3


'''
110. Write a Python program to get numbers divisible by fifteen from a list
using an anonymous function.
'''
import random
n_list = []
while len(n_list) < 10: n_list.append(random.randint(0, 3000))
divisible_of_15 = lambda e : e % 15 == 0
print(f'List of numbers : {n_list}')
print(f'Divisible by 15 : {[x for x in n_list if divisible_of_15(x)]}')
