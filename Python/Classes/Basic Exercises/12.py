#!/usr/bin/env python3


'''
12. Write a Python class named Student with two instances student1, student2 and
assign values to the instances' attributes.
Print all the attributes of the student1, student2 instances with their values
in the given format.
'''


class Student:
    pass

student1 = Student()
student2 = Student()

student1.student_name = "Juan"
student2.student_name = "Carlos"

student1.student_id = "C137"
student2.student_id = "H304"

print(student1.__dict__)
print(student2.__dict__)
