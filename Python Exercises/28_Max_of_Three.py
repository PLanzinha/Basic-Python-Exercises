# Exercise 28 -  Max Of Three

# Implement a function that takes as input three variables, and returns the largest of the three. Do this without
# using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need
# is some variables and if statements!


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif a >= b and b <= c:
        return c
    elif a <= b and b >= c:
        return b


if __name__ == "__main__":
    three_input = input("Enter three variables of any size separated by commas (,).\n")
    a, b, c = map(int, three_input.split(','))
    result = max_of_three(a, b, c)
    print(f"From the three variables chosen, {a}, {b}, and {c}, the largest of the three is {result}.")



