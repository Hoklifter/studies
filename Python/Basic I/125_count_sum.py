#!/usr/bin/env python3


'''
125. Write a Python program to sum all counts in a collection.
'''

import collections

nums = 2, 3, 4, 6, 5, 4, 4
counter = dict(collections.Counter(nums))
summed = sum(counter.values())
sum_representation = "+".join([str(x) for x in counter.values()])

print(f'{nums = }\n{counter = }\n{summed = } ({sum_representation})')
