# Exercise 12 -  List Ends


# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a = [1, 2, 3, 4, 5, 30, 60, 90]


def list_ends(list):
    return [list[0], list[-1]]


print(list_ends(a))
