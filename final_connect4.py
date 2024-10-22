# Author   : Gerania Cedeno
# Email    : geraniaceden@mass.edu
# Spire ID : 34726464

def make_empty_board(nrows, ncols):
# nrows = number of rows, strings
# ncols = number of columns, "."
     return ["." * ncols for elem in range(nrows)]
# return ^ generates a list that creates a list of strings
# for return ^ , the string will repeat the "." character ncols times (7)
# for return ^ , range(nrows) generates a sequence from 0 to nrows -1 (range(start at, stop before (nrows input - 1), step +1)
# for return ^ , elem is a placeholder to represent each number inside the range 
# "." = empty spot
print(make_empty_board(6, 7))
# print(make_empty_board(number of rows you want, number of columns you want))

# def print_board(game_board):
#     game_board = [" X ", " 0 ", "   " ]
#     ncols = [" | "]
#     nrows = ["---+"]
# print(make_empty_board(6,7))

# def verify_board():

# def verify_move():

# def update_board():

# def has_won():
