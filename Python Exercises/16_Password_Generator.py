import random
import string


# Exercise 16 - Password Generator

# Write a password generator in Python. Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def pass_gen(a):
    lower_letter = "abcdefghijklmnopqrstuvxzy"
    higher_letter = "ABCDEFGHIJKLMNOPQRSTUVXZY"
    numbers = "1234567890"
    signs = "~`!@#$%^&*()_-+={[}]|:;<,>.?/"
    weak = ["HELLO_WORLD", "he11oW0rld", "password", "Venezia4ever", "Shakira", "TreeOfLife"]
    strong = random.randint(17, 32)
    if a == 'weak':
        return random.choice(weak)
    elif a == 'strong':
        b = "".join(random.choice(lower_letter + higher_letter + numbers + signs) for c in range(strong))
        return b
    else:
        return print("Input is invalid!")


f = str(input("Please input if you would like to generate between either a weak password or a strong password!\n"))
print(pass_gen(f))


# attempting with string

def pass_gen(a):
    weak = ["HELLO_WORLD", "he11oW0rld", "password", "Venezia4ever", "Shakira", "TreeOfLife"]

    if a == 'weak':
        return random.choice(weak)
    elif a == 'strong':
        strong = random.randint(17, 32)
        c = string.ascii_letters + string.digits + string.punctuation
        d = ''.join(random.choice(c) for _ in range(strong))
        return d
    else:
        return "Input is invalid!"


f = str(input("Please input if you would like to generate between either a weak password or a strong password!\n"))
print(pass_gen(f))
