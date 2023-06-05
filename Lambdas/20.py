#!/usr/bin/env python3


'''
20.

Write a Python program to find the numbers in a given string and store them in a list.
Afterward, display the numbers that are longer than the length of the list in sorted form.
Use the lambda function to solve the problem.

Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56
'''


string = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'

splitted_string = string.split()
splitted_string = [int(x) for x in splitted_string if x.isnumeric()]
splitted_string.sort()
bigger_than_splitted = lambda s : True if s > len(splitted_string) else False

result = filter(bigger_than_splitted, splitted_string)
result = [str(x) for x in result]

print(f"""Original string:
{string}
Numbers in sorted form:
{' '.join(result)}""")

# string_nums = re.split(r'', string)
# while '' in string_nums: string_nums.remove('')
# print(string_nums)
