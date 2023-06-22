#!/usr/bin/env python3


'''
8. Write a Python program to create two empty classes, Student and Marks.
Now create some instances and check whether they are instances of the said
classes or not. Also, check whether the said classes are subclasses of the
built-in object class or not.
'''


class Student:
    pass


class Marks:
    pass


s1 = Student()
m1 = Marks()

print(isinstance(s1, Student))
print(isinstance(m1, Marks))
print(isinstance(m1, Student))
print(isinstance(s1, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))
