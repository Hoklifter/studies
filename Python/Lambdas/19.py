#!/usr/bin/env python3


'''
19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']
'''


anagram = lambda s : sorted('abcd') == sorted(s)
l = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
anagrams_in_l = list(filter(anagram, l))


print(f"""Orginal list of strings:
{l}
Anagrams of 'abcd' in the above string:
{anagrams_in_l}""")
