'''
1.


Write a Python program.


create a lambda function that
    adds 15 to a given number passed in as an argument.


create a lambda function that
    multiplies argument x with argument y and prints the result.


Sample Output:
25
48
'''

add_15 = lambda num : num + 15
#I know i could just do print(x * y) but i tried to make as close as possible of the exercise request.
multiply = lambda x, y : (z := x * y, print(z))


num = 25
x, y = 25, 48


print(add_15(num))
multiply(x, y)