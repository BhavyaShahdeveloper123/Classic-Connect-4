import numpy as np

rows=6
column=7


def actualboard():
    board=np.zeros((6,7))
    return board
board=actualboard()


def location(board,col):# valid location
#check if it has not been filled since there are 5 rows
    return board[5][selection]==0

def makeamove(board,row,selection,piece):# drop piece
    board[row][selection]=piece

def newrow(board,selection):
    for i in range(rows):
        if board[i][selection]==0:
            return i
# to make sure that the chips fall into the board
def print_board(board):
    print(np.flip(board,0))
# Function that checks all winning posibilities from including vertical, horizontal, negative diaganol and positive Diaganol
def winning_move(board,piece):
    #negative Diagnols for winning moves
    for c in range(column-3):
        for r in range(3,rows):
            if board[r][c]==piece and board[r-1][c+1]== piece and board[r-2][c+2] and board[r-3][c+3]==piece:
                return True
    #Horizontal Location For Winning Moves
    for c in range(column-3):
        for r in range(rows):
            if board[r][c]==piece and board[r][c+1]== piece and board[r][c+2] and board[r][c+3]==piece:
                return True
    #vertical Location for winning moves
    for c in range(column):
        for r in range(rows-3):
            if board[r][c]==piece and board[r+1][c]== piece and board[r+2][c] and board[r+3][c]==piece:
                return True
    # positive diaganols for winning moves
    for c in range(column-3):
        for r in range(rows-3):
            if board[r][c]==piece and board[r+1][c+1]== piece and board[r+2][c+2] and board[r+3][c+3]==piece:
                return True

    
    
print_board(board)
# while loop that asks for the input of the player
# determines whose turn it is
finished=True
playerturn=0
while finished:
    if playerturn==0:
        selection= int(input("player 1 input a number from 0-6"))

        if location(board,selection):
            row=newrow(board,selection)
            makeamove(board,row,selection,1)

            if winning_move(board,1):
                print("player one wins! Congratulations")
                print("better luck next time player 2!")
                finished=False
            
    elif playerturn!=0:
        selection= int(input("player 2 input a number from 0-6"))

        if location(board,selection):
            row=newrow(board,selection)
            makeamove(board,row,selection,2)

            if winning_move(board,1):
                print("player two wins! Congratulations")
                print("better luck next time player 1!")
                finished=False

    # helps alternate between the players
    playerturn=playerturn+1
    playerturn= playerturn % 2

    print_board(board)
        
        
        
