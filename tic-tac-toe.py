# 3 by 3 board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min = 1
max = 9
player_symbol = 'O'
computer_symbol = 'x'
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
def DisplayBoard(board):
    for row in board:
        print(row)

#
# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision
#
def EnterMove(board):
    move = int(input("Pick a move: "))
    if move < min or move > max:
        print("Illegal move")
        return
    for row in board:
        if move in row:
            position = row.index(move)
            row[position] = player_symbol

#
# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
def MakeListOfFreeFields(board):
    list = []
    for row in range(len(board)):
        for col in range(len(row)):
            if item is not player_symbol or computer_symbol:
                list.append((row,col))
    print(list)
    return list

DisplayBoard(board)
EnterMove(board)
MakeListOfFreeFields(board)
DisplayBoard(board)
