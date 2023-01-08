# Exercise 3 -  List Less Than Ten
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less
# than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original
# list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Array slice with 5 included

print(a[:5])

# Printing out every element of the list that is below 5

for items in a:
    if items < 5:
        print(items)

# Append each item to the list

b = []

for items in a:
    if items < 5:
        b.append(items)
        print(b)

# List comprehension

items = [item for item in a[:5] if item < 5]
print(items)

# Ask the user for input to filter the list with

number = int(input("Input a number to filter the list by, highest number is 89:\n"))
for i in a:
    if i < number:
        print(i)
