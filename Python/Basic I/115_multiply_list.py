#!/usr/bin/env python3


'''
115. Write a Python program to compute the product of a list of integers
(without using a for loop).
'''


def create_list():
    from random import randint
    l = []
    while len(l) < 5:
        l.append(randint(0, 10))
    return l


def multiply_list(n_list):
    n_list = n_list[:]
    while len(n_list) > 1:
        n_list[0] *= n_list[1]
        del n_list[1]
    return n_list[0]


nums = create_list()
multiplied_nums = multiply_list(nums)

print(f'{nums = }\n{multiplied_nums = }')
