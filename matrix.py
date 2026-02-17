def sumofmatrix(l1,l2,l3,m,n):
    for i in range(m):
        for j in range(m):
            l3[i][j]=l1[i][j]+l2[i][j]


def sumofelements(l,m,n):
    s=0
    for i in range(m):
        s=s+sum(l[i])
    return s

def matrixmul(l1,l2,l4,m,n):
    for i in range(m):
        for j in range(n):
            for k in range(m):
                temp=l1[i][k]*l2[k][j]
                l4[i][j]=l4[i][j]+temp


def printm(l,m,n):
  print("printing matrix")
  for i in range(m):
        for j in range(m):
            print(l[i][j],end=" ")
        print()

def init(l,m,n):
    for i in range(m):
        temp=[0 for i in range(m)]
        l.append(temp)

def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input("Enter row").split()]
        l.append(temp)

def sumofrows(l1,m,n):
    for i in range(m):
        print("The",i,"row sum is",sum(l1[i]))

def sumofcol(l,m,n):
    sum=0
    for i in range(m):
        for j in range(n):
            sum=sum+l[j][i]
        print("The",i,"column wise sum is ",sum)
        sum=0
def sumofdiag(l,m,n):
    sum=0
    for i in range(m):
        for j in range(n):
            if i==j:
                sum=sum+l[i][j]
    print("The sum of diag elements is ",sum)

def sumofoppdiag(l,m,n):
    sum=0
    for i in range(m):
        sum=sum+l[i][len(l[i])-i-1]
    print("The sum of opposite diagnal elemets is ",sum)

def Transpose(l,m,n):
    for i in range(m):
        for j in range(m):
            print(l[j][i],end=" ")
        print()
def isIdentity(l,m,n):
    for i in range(m):
        for j in range(m):
            if i==j and l[i][j]!=1:
                return False
            elif i!=j and l[i][j]!=0:
                return False
    return True
def swaprows(l,m,n,r1,r2):
    l[r1-1],l[r2-1]=l[r2-1],l[r1-1]

def swapcol(l,m,n,c1,c2):
    for i in range(m):
        l[i][c1-1],l[i][c2-1]=l[i][c2-1],l[i][c1-1]
def swapdiag(l,m,n):
    for i in range(m):
        for j in range(m):
            if i==j:
                l[i][j],l[i][m-i-1]=l[i][m-i-1],l[i][j]

def rotatematrix(l,m,n):
    ls=[]
    for i in range(m):
        temp=[0 for i in range(m)]
        ls.append(temp)
    for i in range(m):
        for j in range(m):
            ls[i][j]=l[j][m-i-1]
    printm(ls,m,n)

l1=[]
l2=[]
l3=[]
l4=[]
m=int(input("Enter the number of row "))
n=int(input("Enter the number of Columns "))
read(l1,m,n)
#read(l2,m,n)
printm(l1,m,n)
#printm(l2,m,n)
#init(l3,m,n)
#init(l4,m,n)
#sumofmatrix(l1,l2,l3,m,n)3
#printm(l3,m,n)
#matrixmul(l1,l2,l4,m,n)
#printm(l4,m,n)
sumofrows(l1,m,n)
sumofcol(l1,m,n)
sumofdiag(l1,m,n)
sumofoppdiag(l1,m,n)
Transpose(l1,m,n)
print("Is the matrix Identity",isIdentity(l1,m,n))
#swaprows(l1,m,n,1,3)
#printm(l1,m,n)
#swapcol(l1,m,n,1,2)
#printm(l1,m,n)
#swapdiag(l1,m,n)
#printm(l1,m,n)
rotatematrix(l1,m,n)