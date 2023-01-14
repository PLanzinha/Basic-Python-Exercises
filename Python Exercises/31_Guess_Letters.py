# Exercise 31 -

# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to
# guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the
# actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
# guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
# infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed
# and display a different message if the player tries to guess that letter again. Remember to stop the game when all
# the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number
# of guesses the player has remaining - we will deal with those in a future exercise.


def draw_board(word, guessed_letters):
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_"

    print(hidden_word)


def word_guess():
    word = 'EVAPORATE'

    guessed_letters = set()

    while True:
        attempt_counter = len(guessed_letters) + 1
        wrong_attempt_counter = 0

        draw_board(word, guessed_letters)

        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You have already inputted that letter before, try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Guess is correct.")
        else:
            wrong_attempt_counter += 1
            print("Guess is wrong try again.")

        print(guessed_letters)
        # print(attempt_counter)

        if all(letter in guessed_letters for letter in word):
            draw_board(word, guessed_letters)
            print(f"The secret word was indeed '{word}' congratulations! And it only took you {wrong_attempt_counter}"
                  f" attempts, with only {wrong_attempt_counter} wrong attempts!")
            break


if __name__ == "__main__":
    word_guess()
