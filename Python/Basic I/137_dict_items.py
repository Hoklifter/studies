#!/usr/bin/env python3


'''
137. Write a Python program to extract a single key-value pair
from a dictionary into variables.
'''
dictionary = {
    1 : 'Foo',
    2 : 'Bar'
}
dictionary_items = [{x : y} for x, y in list(dictionary.items())]
print(f'{dictionary = }')
print(f'{dictionary_items = }')
print(dictionary_items[0])
print(dictionary_items[1])
