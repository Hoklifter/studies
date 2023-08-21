#!/usr/bin/env python3


'''
148. Write a Python function to find the maximum and minimum numbers from a
sequence of numbers.
Note: Do not use built-in functions.
'''
def maximum_minimum(seq):
    maximum = minimum = seq[0]
    for x in seq:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    return maximum, minimum

sequence = 1, 3, 9, 4, 0, -5,
maximum, minimum = maximum_minimum(sequence)
print(f'Maximum and minimum values in {sequence} are {maximum, minimum}.')
