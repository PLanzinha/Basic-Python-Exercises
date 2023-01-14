# Exercise 26 - Check Tic Tac Toe

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more
# than half an hour of coding, so we’re doing it in pieces.
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the
# moves were made.

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


if __name__ == "__main__":
    result_1 = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    print("Result game 1")
    draw_board(result_1)

    result_2 = [[2, 2, 1],
                [1, 2, 1],
                [1, 2, 2]]

    print("Result game 2")
    draw_board(result_2)

    result_3 = [[2, 2, 1],
                [1, 2, 1],
                [1, 2, 2]]

    print("Result game 3")
    draw_board(result_3)

