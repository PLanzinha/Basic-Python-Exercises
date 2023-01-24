# Exercise 39 - Character Input Datetime

# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old), except don’t
# explicitly write out the year. Use the built-in Python datetime library to make the code you write work during
# every year, not just the one we are currently in.

import datetime

date = datetime.datetime
date.now()
print(date.now().year)


def hundred_years_age():
    name_input = input("Hello, before we start, what is your name?\n")

    now = datetime.datetime.now().year

    age_input = input(f"Now, the current year is {now}, so how old are you {name_input}?\n")

    years_left = int(now) - int(age_input) + 100

    print(f"Then i must inform you, {name_input}, that you will turn 100 by the year {str(years_left)}")


if __name__ == "__main__":
    hundred_years_age()
