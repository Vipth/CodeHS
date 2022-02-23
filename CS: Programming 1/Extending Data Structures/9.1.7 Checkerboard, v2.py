# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        # [str(x) for x in board[i]]
        print(" ".join([str(x) for x in board[i]]))

# Your code here...
board = []
for i in range(8):
    board.append([0] * 8)

for i in range(len(board)):
    for j in range(8):
        if j % 2 == 1 and i % 2 == 0:
            board[i][j] = 1
        elif j % 2 == 0 and i % 2 == 1:
            board[i][j] = 1
# Sets the board to:
# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        # [str(x) for x in board[i]]
        print(" ".join([str(x) for x in board[i]]))

# Your code here...
board = []
for i in range(8):
    board.append([0] * 8)

for i in range(len(board)):
    for j in range(8):
        if j % 2 == 1 and i % 2 == 0:
            board[i][j] = 1
        elif j % 2 == 0 and i % 2 == 1:
            board[i][j] = 1
# Sets the board to:
# [0, 1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 0, 1, 0]
    
print_board(board)
