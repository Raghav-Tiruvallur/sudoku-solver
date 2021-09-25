board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solveBoard(board):
    checkIfEmpty=findEmptySpots(board)
    displayBoard(board)
    if checkIfEmpty is None:
        return True
    else:
        row,col=checkIfEmpty
        for i in range(1,10):
            if isValid(board,i,checkIfEmpty):
                board[row][col]=i
                if solveBoard(board):
                    return True
            board[row][col]=0
    return False


def isValid(board,value,position):
    row,col=position
    for i in range(len(board[0])):
        if board[row][i]==value and i!=row:
            return False
    for j in range(len(board)):
        if board[j][col]==value and j!=col:
            return False
    #Find if value exists in my box
    bx=col//3
    by=row//3
    for i in range(by*3,by*3+3):
        for j in range(bx*3,bx*3+3):
            if board[i][j]==value and (i,j)!=position:
                return False
    return True 

def displayBoard(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("------------------------------")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end=" ")

def findEmptySpots(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    return None


solveBoard(board)
displayBoard(board)