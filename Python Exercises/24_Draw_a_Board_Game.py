# Exercise 24 - Draw A Game Board

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3,
# and Part 4. Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s
# print statement.

def draw_board(board):
    for i in range(board):
        print(" ---" * board)

        print("|   " * (board + 1))
    print(" ---" * board)


if __name__ == "__main__":
    draw_input = int(input("Select the size of the board you wish to draw.\n"))
    draw_board(draw_input)
