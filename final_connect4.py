# Author   : Gerania Cedeno
# Email    : geraniaceden@mass.edu
# Spire ID : 34726464

def make_empty_board(nrows, ncols):
# nrows = number of rows, strings
# ncols = number of columns, "."
     return ["." * ncols for elem in range(nrows)]
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
