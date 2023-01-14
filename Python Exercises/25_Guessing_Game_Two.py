# Exercise 25 - Guessing Game Two

# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it. This time,
# we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The
# program will guess a number, and you, the user, will say whether it is too high, too low, or your number. At the
# end of this exchange, your program should print out how many guesses it took to get your number. As the writer of
# this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply
# start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal
# guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase
# / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!

import random


def guess_game():
    user_input = int(input("Please write a number from o to 100 so the computer can try and guess!\n"))
    machine_guess = random.randint(0, 100)
    counter = 0
    while True:
        print(machine_guess)
        question = str(input("Did the machine guess the number correctly? Answer with 'y' or 'n' or 'e' to exit.\n"))
        machine_guess = random.randint(0, 100)
        counter += 1
        if question == 'y':
            if machine_guess == user_input:
                print(f"It is indeed correct! Congratulations! Only needed {counter} tries to guess the number.")
                counter += 1
            elif machine_guess >= user_input:
                print("No the user is wrong, the machine didn't guess right the number needed is higher! Please try "
                      f"again! Number of tries {counter}.")
                counter += 1
            elif machine_guess <= user_input:
                print("No the user is wrong, the machine didn't guess right the number needed is lower! Please try "
                      f"again! Number of tries {counter}.")
                counter += 1
        elif question == 'n':
            if machine_guess == user_input:
                print(f"No the user is wrong, the machine guess right! Number of tries {counter}.")
                counter += 1
            elif machine_guess >= user_input:
                print(f"Yes the user is correct! Machine input is higher! Please try again. Number of tries {counter}.")
                counter += 1
            elif machine_guess <= user_input:
                print(f"Yes the user is correct! Machine input is lower! Please try again. Number of tries {counter}.")
                counter += 1
        if question == "e":
            i = False


if __name__ == "__main__":
    guess_game()


