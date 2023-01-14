import random


# Exercise 18 - Cows And Bulls

# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.


def num_gen():
    return str(random.randint(0000, 9999))


def cow_bull(num, attempt):
    cow = 0
    bull = 0
    for c in range(4):
        if num[c] == attempt[c]:
            cow += 1
        elif attempt[c] in num:
            bull += 1
    return cow, bull


def main():
    print("This is the game of cows and bulls, try to guess the correct number!")
    print("Each time you correctly guess a number, you get a bull, the game finishes when you get 4 bulls.")
    gen = num_gen()
    print(gen)
    num_attempt = 0

    while True:
        player_input = input("Please write a 4 digit number to play or write 'exit' to stop!\n")

        if player_input.lower() == 'exit':
            break
        elif len(player_input) != 4 or not player_input.isdigit():
            num_attempt += 1
            print("Please enter a valid 4 digit number to play!")
            continue

        cow, bull = cow_bull(player_input, gen)

        if gen == player_input:
            num_attempt += 1
            print(f"You have won! It only took you {num_attempt} to guess the number {gen}")
            print("Let's play again with a new random number!")
            gen = num_gen()
            num_attempt = 0
        else:
            num_attempt += 1
            print(f"Unfortunately its wrong, you have got {num_attempt} bull, and got {cow} cow right!\n")


if __name__ == "__main__":
    main()
