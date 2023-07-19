#!/usr/bin/env python3


'''
18. Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
'''


s_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindrome = lambda s : True if s == s[::-1] else False
p_list = list(filter(palindrome, s_list))


print(f"""Orginal list of strings:
{s_list}
List of palindromes:
{p_list}""")
