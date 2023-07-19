#!/usr/bin/env python3


'''
6. Write a Python program that accepts a sequence of comma-separated numbers
from the user and generates a list and a tuple of those numbers.

Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

data = input('''Type numbers separated by commas (Ex: 1, 2, 3, 3, 4):
= ''').replace(' ', '').split(',')
print(f'''List : {data}
Tuple : {tuple(data)}''')
