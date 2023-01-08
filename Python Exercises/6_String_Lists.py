# Exercise 6 - String Lists

# Ask the user for a string and print out whether this string is a
# palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

greeting = "Welcome to the Palindrome Test"

palindrome = input(greeting + ", please make your input and we'll evaluate if its a Palindrome:\n")
rev_palindrome = palindrome[::-1]

if rev_palindrome == palindrome:
    print("Input is a Palindrome!")
else:
    print("Input is not a Palindrome!")
