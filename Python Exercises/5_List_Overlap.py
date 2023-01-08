# Exercise 5 - List Overlap

# Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 9, 12, 13, 21, 34, 55, 89, 110]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 31, 34, 42, 50, 55, 89]

for i in range(len(a)):
    if a[i] in b:
        print(a[i])

a = [1, 1, 2, 3, 5, 8, 9, 12, 13, 21, 34, 55, 89, 110]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 31, 34, 42, 50, 55, 89]

c = list(b)
c.extend(
    x for x in a if x not in c)
print(sorted(c))

a = [1, 1, 2, 3, 5, 8, 9, 12, 13, 21, 34, 55, 89, 110]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 31, 34, 42, 50, 55, 89]

for item in a:
    if item not in b:
        b.append(item)
print(sorted(b))
