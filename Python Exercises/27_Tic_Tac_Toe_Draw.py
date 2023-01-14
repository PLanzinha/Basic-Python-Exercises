# Exercise 27 - Tic Tac Toe Draw

# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information
# about a tic-tac-toe game. In a tic-tac-toe game, the “game server” needs to know where the Xs and Os are in the
# board, to know whether player 1 or player 2 (or whoever is X and O won).

# There has also been an exercise about drawing the actual tic-tac-toe game-board using text characters.

# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an
# X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking
# the user for a coordinate of where they want to place their piece.


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


if __name__ == "__main__":
    tic_tac_board = 3
    board = [[0] * tic_tac_board for _ in range(tic_tac_board)]

    draw_board(board)

    for turn in range(tic_tac_board * tic_tac_board):
        current_player = turn % 2 + 1
        update_board(board, current_player)
        draw_board(board)
