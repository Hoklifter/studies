#!/usr/bin/env python3


'''
15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
'''


a = [1, 2, 3]
b = [4, 5, 6]


add_lambda = lambda x, y : x + y
new_list = [x for x in map(add_lambda, a, b)]


print(new_list)
