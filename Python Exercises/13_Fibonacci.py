# Exercise 13 - Fibonacci

# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci sequence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(a):
    if a <= 0:
        return 'With that input there is no corresponding number for the fibonacci sequence.'
    elif a == 1:
        return [1]
    elif a == 2:
        return [1, 1]
    else:
        numbers = [1, 1]
        [numbers.append(numbers[-1] + numbers[-2]) for b in range(a - 2)]
        return numbers


c = int(input('How many numbers of the Fibonacci sequence would you like to print? \n'))
print(fibonacci(c))
