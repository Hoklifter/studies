#!/usr/bin/env python3
'''4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :[
    {
        'make': 'Nokia',
        'model': 216,
        'color': 'Black'
    },
    {
        'make': 'Mi Max',
        'model': '2',
        'color': 'Gold'
    },
    {
        'make': 'Samsung',
        'model': 7,
        'color': 'Blue'
    }
]
Sorting the List of dictionaries :[
    {
        'make': 'Nokia',
        'model': 216,
        'color': 'Black'
    },
    {
        'make': 'Samsung',
        'model': 7,
        'color': 'Blue'
    },
    {
        'make': 'Mi Max',
        'model': '2',
        'color': 'Gold'
    }
]'''

import json
dict_list = [
    {
        'make': 'Nokia',
        'model': 216,
        'color': 'Black'
    },
    {
        'make': 'Mi Max',
        'model': '2',
        'color': 'Gold'
    },
    {
        'make': 'Samsung',
        'model': 7,
        'color': 'Blue'
    }
]

sorted_list = dict_list[:]
sorted_list.sort(key=lambda element: element['color'])


pretty_print = lambda dict_list : json.dumps(dict_list, indent=4)


print('Original list of dictionaries :\n')
print(pretty_print(dict_list))
print('Sorting the List of dictionaries :\n')
print(pretty_print(sorted_list))
