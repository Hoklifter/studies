#!/usr/bin/env python3


'''
16.

Write a Python program to find the second lowest total marks of any student(s)
from the given names and marks of each student using lists and lambda. Input the
number of students, the names and grades of each student.

Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR
'''


students_grades = [
    ['S ROY', 1.0],
    ['B BOSE', 3.0],
    ['N KAR', 2.0],
    ['C DUTTA', 1.0],
    ['G GHOSH', 1.0]
]


sorted_grades = sorted(students_grades, key=lambda l : l[1])

for pos, x in enumerate(sorted_grades):
    if sorted_grades[pos-1][1] < x[1]:

        sec_small_grade = x

        print(f"Input number of students: {len(students_grades)}")
        for y in students_grades: print(f"Name: {y[0]}\nGrade: {y[1]}")
        print(f"Names and Grades of all students:\n{students_grades}")
        print(f"Second lowest grade: {sec_small_grade[1]}")
        print(f"Names: {sec_small_grade[0]}")

        break
