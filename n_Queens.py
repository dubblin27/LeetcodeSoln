
def isSafe(mat,r,c) :
    #to check if 2 Queens are in the same coloumn 
    for i in range(r):
        if mat[i][c] == 1:
            return False 
    
    i,j = r,c 
    #to check Left diagonal '\'
    while i >= 0 and j >= 0 : 
        if mat[i][j] == 1 : 
            return False
        i -=1
        j -=1 
    
    i,j = r,c 
    #to check right diagonal '/'
    while j < N and i >= 0 :
        if mat[i][j] == 1 :
            return False
        j+=1 
        i-=1
    
    return True


def nQueen(mat,r):
    # if N Queens are placed = print results
    if r == N : 
        print(mat)
        return
    # Placing each queen at a position and checking if valid using recursion
    for i in range(N):
        if isSafe(mat,r,i):
            #placing queen
            mat[r][i] = 1
            # recurion for next row
            nQueen(mat,r+1)
            #backtrack and cancel it
            mat[r][i] = 0

N = int(input("Enter Number of Rows/Cols : "))
mat = [[0 for i in range(N)] for i in range(N)]
nQueen(mat,0)