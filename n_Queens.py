
def isSafe(mat,r,c) : 
    for i in range(r):
        if mat[i][c] == 1:
            return False 
    
    i,j = r,c 

    while i >= 0 and j >= 0 : 
        if mat[i][j] == 1 : 
            return False
        i -=1
        j -=1 
    
    i,j = r,c 

    while j < N and i >= 0 :
        if mat[i][j] == 1 :
            return False
        j+=1 
        i-=1
    
    return True


def printsoln(mat):
    for i in range(N) : 
        print(mat[i])
    print()

def nQueen(mat,r):
    if r == N : 
        printsoln(mat)
        return
    
    for i in range(N):
        if isSafe(mat,r,i):
            mat[r][i] = 1
            nQueen(mat,r+1)
            mat[r][i] = 0

N = int(input("Enter Number of Rows/Cols : "))
mat = [[0 for i in range(N)] for i in range(N)]
nQueen(mat,0)