# Exercise 8 - Rock Paper Scissors
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats Scissors.
# Scissor beats paper.
# Paper beats rock.
choices = ["rock", "paper", "scissors"]
i = True

while True:
    player_1 = input('Player 1 please input one of the following, "rock", "paper" or "scissors"\n').lower()
    player_2 = input('Player 2 please input one of the following, "rock", "paper" or "scissors"\n').lower()

    if player_1 or player_2 not in choices:
        print("Invalid input please input answer only with 'rock', 'paper' or 'scissors'!")
        break
    if player_1 == player_2:
        print("its a Tie")
    elif player_1 == "rock" and player_2 == "scissors":
        print("Player 1 Wins!")
    elif player_1 == "scissors" and player_2 == "rock":
        print("Player 2 Wins!")
    elif player_1 == "scissors" and player_2 == "paper":
        print("Player 1 Wins!")
    elif player_1 == "paper" and player_2 == "scissors":
        print("Player 2 Wins!")
    elif player_1 == "rock" and player_2 == "paper":
        print("Player 2 Wins!")
    elif player_1 == "paper" and player_2 == "rock":
        print("Player 1 Wins!")
    h = input('Type "no" to quit or "yes" to continue playing.\n').lower()
    if h == "no":
        i = False
    elif h == "yes":
        i = True
    else:
        print(input('Invalid Answer please input only "yes" or "no".\n'))

