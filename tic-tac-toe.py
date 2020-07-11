# author: farah alyasari

# packages
import random

# 3 by 3 board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min = 1
max = 9
player_symbol = "O"
computer_symbol = "X"
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
def DisplayBoard(board):
    for row in board:
        print(row)

#
# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision,
# the number must be valid and cannot point to a field that's already occupied
#
def EnterMove(board):
    move = 0
    while True:
        try:
            move = int(input("Pick a move: "))
            if move > max or move < min:
                print("Illegal move")
            else:
                break
        except ValueError:
            print("Illegal value")
        except:
            print("unknown error")
    for row in board:
        if move in row:
            move_position = row.index(move)
            row[move_position] = player_symbol

#
# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
def MakeListOfFreeFields(board):
    list = []
    counter = 0
    for row in board:
        for col in row:
            if col != player_symbol and col != computer_symbol:
                row_position = board.index(row)
                col_position = row.index(col)
                list.append((row_position,col_position))
    return list

#
# the function analyzes the board status in order to check if
# the player using 'O's or 'X's has won the game
#
def VictoryFor(board, sign):

#
# the function draws the computer's move and updates the board
# this function has an opportunity to incorporate artifical intelligence, but now it randomly generates a move based on the available position
#
def DrawMove(board):
    try:
        sequence = MakeListOfFreeFields(board)
        move = random.choice(sequence)
        row = move[0]
        col = move[1]
        board[row][col] = computer_symbol
    except IndexError:
        print("The game should have ended")
    except:
        print("unkown error")

def TicTacToe(board):
    while True:
        DrawMove(board)
        DisplayBoard(board)
        EnterMove(board)
        DisplayBoard(board)

TicTacToe(board)
