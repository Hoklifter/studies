#!/usr/bin/env python3

'''
35. Write a Python program that returns true if the two given integer values
are equal or their sum or difference is 5.
'''
def is_equal_or_sum_difference_equals_5(a, b):
    if any([a == b, a + b == 5, abs(a - b) == 5]):
        return True
    return False

print(is_equal_or_sum_difference_equals_5(10, 10))
print(is_equal_or_sum_difference_equals_5(20, 20))

print(is_equal_or_sum_difference_equals_5(1, 4))
print(is_equal_or_sum_difference_equals_5(10, -5))

print(is_equal_or_sum_difference_equals_5(10, 5))
print(is_equal_or_sum_difference_equals_5(15, 20))

print(is_equal_or_sum_difference_equals_5(20, 5))
print(is_equal_or_sum_difference_equals_5(20, 10))
