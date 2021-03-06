#Creating the board
board = [' ' for x in range(10)]


#Taking the letters and postion for the board
def insertLetter(letter,pos):
    board[pos] = letter


# Defining the function for the avaliability of the free space
def spaceIsFree(pos):
    return board[pos] == ' '


#Desing the board by taking a function(printBoard) and assining the board keys
def printBoard(board):
    print("\n")
    print('\t    |    |   ')
    print('\t ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('\t    |    |   ')
    print('\t--------------')
    print('\t    |    |   ')
    print('\t ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('\t    |    |   ')
    print('\t--------------')
    print('\t    |    |   ')
    print('\t ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('\t    |    |   ')
    print("\n\n")


#Checking the board is full or !
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


#Checking the cases of the winner
def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or   #Condition for ROWS
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or    
    (b[1] == l and b[4] == l and b[7] == l) or          #Condition for Col.
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or    
    (b[1] == l and b[5] == l and b[9] == l) or          #Condition for Diagonal
    (b[3] == l and b[5] == l and b[7] == l))


#Setting up the Players move 'X'
def playerMove():
    run = True
    while run:
        move = input("Select the position for 'X'  b/w  1 to 9 : ")
        try:            
            move = int(move)                           #If no. is in valid range
            if move > 0 and  move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("\nThis space is occupied")
            else:
                print("Type a no.  b/w  1 and 9 : ")
        
        except:
            print("\nPlease type a number")


#Setting up the Computer's move 'O'
def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]                    #Updating the list
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []                                #Checking all the possible moves
    for i in possibleMoves:                         #For Corner
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:                 #For Center
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:                #For Edges
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


#Select Random
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


#Defining the main()
def main():
    print("   \\                         /")
    print("    \\  WELCOME TO THE GAME  /")
    print("     \\_____________________/")
    print("\n")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("SORRY YOU LOOSE  :( ")
            break

        if not(isWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")          # " TIE GAME "
            else:
                insertLetter('O' , move)
                print("Computer placed an O on position " , move , ":")
                printBoard(board)
        else:
            print("Hurrayyyyyy!! YOU WIN  :) ")
            break




    if isBoardFull(board):
        print("Tie game")


#Restarting the game
while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("\n\n\n")
        main()
    else:
        break