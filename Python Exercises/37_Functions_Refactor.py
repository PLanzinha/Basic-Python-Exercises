# Exercise 37 - Functions Refactor

# One area of confusion for new coders is the concept of functions (which have been addressed on this blog in
# exercise 11 for example). So in this exercise, we will be stretching our functions muscle by refactoring an
# existing code snippet into using functions.
#
# Here is the code snippet to refactor (taken from a correct but very repeated solution to exercise 24 on this website):

print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")


def h_line(size):
    print(" ---" * size)


def v_line(size):
    print("|   " * (size + 1))


def draw_board(board):
    for i in range(board):
        h_line(board)
        v_line(board)
    h_line(board)


if __name__ == "__main__":
    draw_input = int(input("Select the size of the board you wish to draw: "))
    draw_board(draw_input)
