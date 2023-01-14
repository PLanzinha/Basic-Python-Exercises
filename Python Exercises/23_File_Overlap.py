# Exercise 23 - File Overlap

# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a
# list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

a = []

with open('primenumbers.txt') as open_file:
    read_text = open_file.read()
    strip_text = read_text.split('\n')
    all_text = [int(i) for i in strip_text if i.strip()]
    a.extend(all_text)
# print(a)

b = []

with open('happynumbers.txt') as open_file:
    read_text = open_file.read()
    strip_text = read_text.split('\n')
    all_text = [int(i) for i in strip_text if i.strip()]
    b.extend(all_text)
# print(b)

overlap = list(set(a) & set(b))
print(f"The numbers that overlap in both lists are {sorted(overlap)}")
