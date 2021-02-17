def nqns(mat,r):
    if r == n : 
        print(mat)
        return
    for i in range(n):
        if is_safe(mat,r,i) : 
            mat[r][i] = 1
            nqns(mat,r+1)
            mat[r][i] = 0 

def is_safe(mat,r,c):
    for i in range(n):
        if mat[i][c] == 1:
            return False 
    
    i,j = r,c 
    while i>= 0 and j>=0 : 
        if mat[i][j] == 1 : 
            return False 
        i-=1 
        j-=1 
    
    i,j = r,c 
    while i>=0 and j<n:
        if mat[i][j] == 1 : 
            return False 
        i-=1 
        j+=1 
    return True
    
n = int(input("enter the value of rows/cols : ") )
mat = [[0 for i in range(n)]for i in range(n)]
nqns(mat,0)