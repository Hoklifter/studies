#!/usr/bin/env python3


'''
2. Write a Python program to create a class and display the namespace of that class.
'''

class Person:
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height

    def change_name(self, new_name):
        self.name = new_name

for x in Person.__dict__:
    print(x)
