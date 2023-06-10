#!/usr/bin/env python3


'''
3.
Write a Python program to create an instance of a specified class and
display the namespace of the said instance.
'''

class Person:
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height

    def change_name(self, new_name):
        self.name = new_name

p = Person("Adriano", 11, 1.50)

print(p.__dict__)
