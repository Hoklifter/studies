#!/usr/bin/env python3


'''
48. Write a Python program to parse a string to float or integer.
'''

user_input = input('''Give me a number.
= ''')
try:
    data = float(user_input)
    if data.is_integer():
        data = int(data)
except ValueError:
    data = user_input

print(f'''The string "{user_input}" is detected as "{type(data).__name__}" and converts as
{data}''')
