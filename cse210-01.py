import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_",]

currentPlayer = "x"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------------")
    print(board[6] + "|" + board[7] + "|" + board[8])
printBoard(board)   

#take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp -1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Sorry, player is already in that spot!")
        
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    
    elif board[3] == board[4] ==board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] ==board[8] and board[6] != "_":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == [8] and board[2] != "_":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("it is a tie!")
        gameRunning = False
        
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "0"
    else:
        winnerplayer = "x"
        
def checkWin():
    if checkDiag or checkHorizontal or checkRow(board):
        print(f"The winner is {winner}")
        
#computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()
            
#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie()
    switchPlayer()
    computer(board)
    checkWin()
    checkTie()
    

    
    
    