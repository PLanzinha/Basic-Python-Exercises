# Exercise 1 - Character Input
#
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year
# (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

# Extras:
# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

greeting = input("Hello, before we start, what is your name?\n")
current_year = input("Thank you" + " " + greeting + " " + "can you tell the year we are in for starters?\n")
current_age = input("So the year is" + " " + current_year + " " + "and how old are you right now?\n")
years_till = int(current_year) - int(current_age) + 100

print("Then i must inform you, " + greeting + ", you will turn 100 in the year " + str(years_till))
