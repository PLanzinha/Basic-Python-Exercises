# Exercise 14 List Remove Duplicates

# Write a program (function!) that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9, 9, 9, 9, 10, 10, 11]

# Test on using set()
ab = set(a)
print(ab)


def sets(b):
    return list(set(b))


print(sets(a))


# Using the way it was done in exercise 5
def set_loop(c):
    d = []
    for item in c:
        if item not in d:
            d.append(item)
    return d


print(set_loop(a))
