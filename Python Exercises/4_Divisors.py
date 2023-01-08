# Exercise 4- Divisors

# Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors
# of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("Please provide a number:\n"))
a = range(1, number+1)

for items in a:
    print(items)

divisor = int(input("Provide a number to find the divisors of: \n"))
b = []

for c in a:
    if number % c == 0:
        b.append(c)
print(b)
