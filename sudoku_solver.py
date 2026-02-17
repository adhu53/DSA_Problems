def issafe(sudoko,i,j,d):
    #horizontal check
    for col in range(0,9):
        if sudoko[i][col]==d:
            return False
    #Vertical check
    for row in range(0,9):
        if sudoko[row][j]==d:
            return False
    sr=(i//3)*3
    sc=(j//3)*3
    for m in range(sr,sr+3):
        for n in range(sc,sc+3):
            if sudoko[m][n]==d:
                return False
    return True

def sudokosolver(sudoko,i,j):
    if i==len(sudoko):#9
        print("=================")
        printsudoko(sudoko)
        return True
    if j==9:
        return sudokosolver(sudoko, i + 1, 0)
    if sudoko[i][j]!=0:
        return sudokosolver(sudoko,i,j+1)
    for d in range(1,10):
        if issafe(sudoko,i,j,d):
            sudoko[i][j]=d
            sudokosolver(sudoko, i, j+1)
            sudoko[i][j]=0
    return False #if no solution

def printsudoko(sudoko):
    for i in range(len(sudoko)):
        for j in range(len(sudoko)):
            print(sudoko[i][j],end=" ")
        print()

sudoko=[[0,0,0,0,6,8,0,0,3],
        [6,0,0,1,9,7,2,5,0],
        [9,0,5,3,0,0,6,8,7],
        [0,5,0,0,0,3,8,9,0],
        [3,0,0,8,0,0,0,0,0],
        [0,0,0,9,0,6,3,4,0],
        [0,3,0,6,8,0,0,0,9],
        [5,0,0,7,3,0,1,0,2],
        [7,0,4,2,1,0,0,0,0]]
printsudoko(sudoko)
sudokosolver(sudoko,0,0)