# Exercise 38 - f Strings

# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old), except use
# f-strings instead of the + operator to print the resulting output message.


def ask_age():
    name_input = input("Hello, before we start, what is your name?\n")
    year_input = input(f"Thank you {name_input} can you tell the year we are in for starters?\n")
    age_input = input(f"So the year is {year_input} and how old are you right now?\n")

    years_left = int(year_input) - int(age_input) + 100

    print(f"Then i must inform you, {name_input}, that you will turn 100 by the year {str(years_left)}")


if __name__ == "__main__":
    ask_age()
