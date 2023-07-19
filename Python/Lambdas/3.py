'''3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''


t_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]


sorting_lambda = lambda tuple_ : tuple_[1]
t_list.sort(key=sorting_lambda)


print(t_list)
