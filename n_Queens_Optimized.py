def solveNQueens(n):
        def helper(queens,ijdiff,ijsum) :
            p = len(queens) 
            if p == n:
                res.append(queens)
                return None 
            for q in range(n):
                if q not in queens:
                    x = p-q 
                    y = p+q
                    if x not in ijdiff and y not in ijsum:
                        helper(queens+[q], ijdiff+[x], ijsum+[y])
        res = [] 
        
        helper([],[],[])
        print(res)
        return [['0'*j + '1' + '0'*(n-j-1) for j in solution] for solution in res]
n = int(input("Enter Value of N : "))
print(solveNQueens(n))