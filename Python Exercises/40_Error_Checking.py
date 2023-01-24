# Exercise 40 - Error Checking

# Given this solution to Exercise 9, modify it to have one level of user feedback: if the user does not enter a
# number between 1 and 9, tell them. Don’t count this guess against the user when counting the number of guesses they
# used.
import random

a = random.randint(1, 9)
b = 0


def guessing_game():
    number_list = random.randint(1, 9)
    guess_counter = 0

    while True:
        print(number_list)
        guess_input = int(input("Welcome to the guessing game! The objective of this game is to try to guess between "
                                "1 and 9 and find the correct number selected randomly!\n"))
        try:
            if guess_input == number_list:
                guess_counter += 1
                if guess_counter == 1:
                    print(f"You guessed {guess_input} correctly, it took you {guess_counter} try.")
                    guess_counter = 0
                else:
                    print(f"You guessed {guess_input} correctly, it took you {guess_counter} tries.")
                    guess_counter = 0
            elif guess_input <= number_list:
                guess_counter += 1
                print(f"You guessed {guess_input}, unfortunately it is too low, please try again.")
            elif guess_input >= number_list:
                guess_counter += 1
                print(f"You guessed {guess_input}, unfortunately it is too high, please try again.")
        except ValueError:
            print("Input is invalid, please choose a number within the range of 1 to 9.")

        end_game = input("Alternatively, you can write 'e' to exit, 'c' to continue with the same number or 'n' for a "
                         "new number.\n")

        if end_game == 'e':
            return False
        elif end_game == 'c':
            pass
        elif end_game == 'n':
            number_list = random.randint(1, 9)
            pass
        else:
            input("Invalid input. Please write either 'e', 'n' or 'c'.")


if __name__ == "__main__":
    guessing_game()
