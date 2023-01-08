# Exercise 15 - Reverse Word Order

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele
# Then I would see the string shown back to me.
# Michele is name My

a = 'My name is Pedro, nice to meet you'

result = a.split()
print(result)
result2 = result[::-1]
print(result2)


def reverse_order(b):
    c = b.split()
    d = c[::-1]
    return " ".join(d)


f = str(input('Please write a phrase you want to see in a reversed order.\n'))
print(reverse_order(f))
