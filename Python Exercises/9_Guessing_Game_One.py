import random
# Exercise 9 -  Guessing Game One

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

a = random.randint(1, 9)
b = 0

c = True

while c:
    inp = input("Guess if the number is between 1 and 9.\n")
    if inp == str(a):
        b += 1
        print(inp, "You guessed correctly! And only took:", b, "tries")
    elif inp <= str(a):
        b += 1
        print(inp, "Input is too low!")
    elif inp >= str(a):
        b += 1
        print(inp, "Input is too high!")
    d = input('Type "n" to quit or "y" to continue playing \n').lower()
    if d == "no":
        i = False
    elif d == "yes":
        d = True
