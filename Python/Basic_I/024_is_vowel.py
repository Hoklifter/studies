#!/usr/bin/env python3


'''
24. Write a Python program to test whether a passed letter is a vowel or not.
'''
def is_vowel(l):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if l and l.lower() in vowels:
        return True
    return False

print(is_vowel('a'))
print(is_vowel('b'))
print(is_vowel('e'))
print(is_vowel('c'))
print(is_vowel('i'))
print(is_vowel('o'))
print(is_vowel('u'))
