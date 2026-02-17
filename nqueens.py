def issafe(board,i,j):
    #column wise check
    row=i-1
    while row>=0:
        if board[row][j]=="Q":
            return False
        row=row-1
    #diagnoal right up check
    row=i-1
    col=j+1
    while row>=0 and col<len(board):
        if board[row][col]=="Q":
            return False
        row=row-1
        col=col+1
    #diagnoal left up check
    row=i-1
    col=j-1
    while row>=0 and col>=0:
        if board[row][col]=="Q":
            return False
        row=row-1
        col=col-1
    return True



def nqueens(board,i,j):
    if i==len(board):
        printboard(board)
        print()
        return
    for j in range(len(board)):
        if issafe(board,i,j):
            board[i][j]="Q"
            nqueens(board,i+1,j)
            board[i][j]="X"


def printboard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=' ')
        print()
    print()

n=5
board=[["X" for i in range(n)] for i in range(n)]
printboard(board)
nqueens(board,0,0)