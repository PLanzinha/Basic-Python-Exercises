# Exercise 7 - List Comprehensions

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a
# and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [d for d in a if d % 2 == 0]
print(b)

print("Even Numbers List:", [c for c in a if c % 2 == 0])
print("Odd Numbers List:", [c for c in a if c % 2 != 0])
