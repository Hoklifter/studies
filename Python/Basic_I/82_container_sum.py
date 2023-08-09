#!/usr/bin/env python3


'''
82. Write a Python program to calculate the sum of all items of a container
(tuple, list, set, dictionary).
'''


containers = (1, 2, 3), [1, 2, 3], {1, 2, 3}, {'a' : 1, 'b' : 2, 'c' : 3}
for container in containers:
    if not isinstance(container, dict):
        container_sum = sum(container)
    else:
        container_sum = sum(container.values())

    print(f'{container_sum = }')
