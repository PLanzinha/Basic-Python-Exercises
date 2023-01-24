# Exercise 32 - Hangman

# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
# (head, body, 2 legs, and 2 arms) before they lose the game.
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the
# letter and displaying that information to the user. In this exercise, we have to put it all together and add logic
# for handling guesses.
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# Only let the user guess 6 times, and tell the user how many guesses they have left. Keep track of the letters the
# user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:
# When the player wins or loses, let them start a new game. Rather than telling the user "You have 4 incorrect
# guesses left", display some picture art for the Hangman.

import random


def draw_board(word, guessed_letters):
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_"

    print(hidden_word)


def word_guess():
    with open('sowpods.txt', 'r') as open_file:
        read_text = open_file.read()

        lines = read_text.split()

        word = random.choice(lines)
    # print(word)

    guessed_letters = set()
    wrong_attempt_counter = 0

    drawn_parts = [
        "The head has been drawn.",
        "The body has been drawn.",
        "The left arm has been drawn.",
        "The right arm has been drawn.",
        "The right leg has been drawn.",
        "The left leg has been drawn, and the man has hanged!",
    ]

    print("Welcome to the game of Hangman! In this game you have 6 attempts at guessing the word correctly after that "
          "the hangman will be fully drawn and the Player will lose!")

    while True:
        attempt_counter = len(guessed_letters) + 1
        draw_board(word, guessed_letters)

        guess = input("Please try to guess a letter: ").upper()

        if guess in guessed_letters:
            print("You have already inputted that letter before, try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Guess is correct.")
        else:
            print("Guess is wrong try again.\n")
            wrong_attempt_counter += 1

        if 1 <= wrong_attempt_counter <= len(drawn_parts):
            for i in range(wrong_attempt_counter):
                print(f"{i + 1}. {drawn_parts[i]}")

        print(f"\n{guessed_letters}")

        if wrong_attempt_counter == 6:
            print(f"The Player guessed wrongly six times, the player has lost, the secret word was {word}.")

        if all(letter in guessed_letters for letter in word):
            draw_board(word, guessed_letters)
            print(f"The secret word was indeed '{word}' congratulations! And it only took you {attempt_counter}"
                  f" guesses, with only {wrong_attempt_counter} wrong guesses!")
            break


if __name__ == "__main__":
    word_guess()
