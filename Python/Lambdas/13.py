#!/usr/bin/env python3
'''
13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
'''


array = [1, 2, 3, 5, 7, 8, 9, 10]
even = lambda n : True if n % 2 == 0 else False
num_even = 0
num_odd = 0


for x in array:
    if even(x): num_even += 1
    else: num_odd += 1

print(f'''Original arrays:
{array}
Number of even numbers in the above array: {num_even}
Number of odd numbers in the above array: {num_odd}''')
