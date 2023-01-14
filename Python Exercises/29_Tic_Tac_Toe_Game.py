# Exercise 29 - Tic Tac Toe Game

# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge
# in this exercise is to use the functions from those previous exercises all together in the same program to make a
# two-player game that you can play with a friend. There are a lot of choices you will have to make when completing
# this exercise, so you can go as far or as little as you want with it.
#
# Here are a few things to keep in mind:
#
# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
#
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1
# or Player 2.


def draw_board(board):
    for i in board:
        print(" ---" * len(i))
        print("|", end="")

        for cell in i:
            if cell == 0:
                print("   |", end="")
            elif cell == 1:
                print(" X |", end="")
            elif cell == 2:
                print(" O |", end="")

        print(" ")

    print(" ---" * len(board[0]))


def update_board(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-{len(board) - 1}): "))
            col = int(input(f"Player {player}, enter column (0-{len(board[0]) - 1}): "))
            if len(board) > row >= 0 == board[row][col] and 0 <= col < len(board[0]):
                board[row][col] = player
                break
            else:
                print("Input is invalid please try again.")
        except ValueError:
            print("Input is invalid row and column should be numerical values please try again.")


def win_loss_draw_checker(board, player):
    for i in range(len(board)):
        if all(cell == player for cell in board[i]):
            return True

        if all(board[j][i] == player for j in range(len(board))):
            return True

    if all(board[i][i] == player for i in range(len(board))) or \
            all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True

    for row in board:
        if 0 in row:
            return False

    return False


if __name__ == "__main__":
    tic_tac_board = 3
    board = [[0] * tic_tac_board for _ in range(tic_tac_board)]

    draw_board(board)

    for turn in range(tic_tac_board * tic_tac_board):
        current_player = turn % 2 + 1
        update_board(board, current_player)
        draw_board(board)

        if win_loss_draw_checker(board, current_player):
            print(f"Player {current_player} wins!")
            break
