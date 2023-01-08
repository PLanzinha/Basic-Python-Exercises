# Exercise 2 - Odd or Even


# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2? If the number is a multiple of 4,
# print out a different message. Ask the user for two numbers: one number to check (call it num) and one number to
# divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Write any number:\n"))
modul = number % 2

if modul == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")


num = int(input("Write another number:"))
div = int(input("Write a number to divide by:\n"))

if num % div == 0:
    print(div, "divides evenly into", num)
else:
    print(div, "doesn't divide evenly into", num)
