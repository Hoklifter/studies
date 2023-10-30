#!/usr/bin/env python3


'''
150. Write a Python function to check whether a distinct pair of numbers whose
product is odd is present in a sequence of integer values.
'''

def distinct_pair_whose_product_is_odd_in_a_seq(seq):
    whose_product_is_odd = []
    for x in sequence:
        for y in sequence:
            product = x * y
            x_y = sorted((x, y))
            if all([
                y != x,
                x_y not in whose_product_is_odd,
                product % 2 != 0
                ]):
                whose_product_is_odd.append(x_y)
    return whose_product_is_odd

sequence = 3, 4, 5, 2, 4, 3, 5, 67, 9
pairs = distinct_pair_whose_product_is_odd_in_a_seq(sequence)
print(pairs)
