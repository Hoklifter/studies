'''
2.


Write a Python program
    create a function that
        takes one argument, and that argument will be multiplied with an unknown given number.


Sample Output:

Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

'''

def x_ple(x): #triPLE, quadruPLE, quintuPLE
    return lambda unknown : unknown * x

double = x_ple(2)
print(f'The double of 15 is {double(15)}')

triple = x_ple(3)
print(f'The triple of 15 is {triple(15)}')

quadruple = x_ple(4)
print(f'The Quadruple of 15 is {quadruple(15)}')

quintuple = x_ple(5)
print(f'The Quintuple of 15 is {quintuple(15)}')