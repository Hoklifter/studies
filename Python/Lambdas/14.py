#!/usr/bin/env python3


'''
14.
    Write a Python program to filter
a given list to determine if the
values in the list have a length of 6 using Lambda.
    Sample Output:
        Monday
        Friday
        Sunday
'''
len_is_6 = lambda element : True if len(element) == 6 else False
filter_lambda = lambda _list_ : filter(len_is_6, _list_)
weekdays = [

    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"

]
[print(x) for x in filter_lambda(weekdays)]
