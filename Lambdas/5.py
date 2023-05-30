#!/usr/bin/env python3
'''5. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]'''

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_even = lambda num : True if num % 2 == 0 else False
filter_odd = lambda num : False if num % 2 == 0 else True

even_nums = list(filter(filter_even, int_list))
odd_nums = list(filter(filter_odd, int_list,))

print(f'Original list of integers:\n{int_list}')
print(f'Even numbers from the said list:\n{even_nums}')
print(f'Odd numbers from the said list:\n{odd_nums}')
