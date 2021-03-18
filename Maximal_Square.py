class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

#TOP-DOWN = Recursion 

        ROWS, COLS = len(matrix), len(matrix[0])  # initialization
        dp = {} # initialization of map 
        
        def helper(r,c) : 
            if r>= ROWS or c>= COLS : return 0 # if the Val of Rows or Cols goes beyond the limit - > return 0 / Null Value 

            if (r,c) not in dp: # if the points which are to the right, down, digonally down right are not visited again traverse through them
                down = helper(r+1,c)
                right = helper(r,c+1) 
                diag = helper(r+1, c+1) 

                dp[(r,c)] = 0 #basically initialize them with 0

                if matrix[r][c] == "1" : # if the current node is 1
                    dp[(r,c)] = 1+min(down,right,diag) # add the cache value to the min value + 1, as the current val is also 1 
                    # if we add max value .. some other node value can be 0 and it will be missed
            return dp[(r,c)] #return the cache value
        
        helper(0,0)
        return max(dp.values()) **2 # from the cache we need to find the max and **2 as it is a square 
        
#BOTTOM - UP = Using FOR LOOP 
#Without using extra space 
        
        m,n = len(matrix) , len(matrix[0]) 
        Mx = 0 # initializing the max Value as 0
        
        for i in matrix[0] : #checking the first row, if it contains 1 the initialize the max value as 1
            if i == "1" : 
                Mx = 1 
                break 
        
        if Mx == 0: # if still the max value remains 0 
            for i in range(m) : # checking the first col
                if matrix[i][0] == "1" : 
                    Mx = 1
                    break 
        
        for i in range(1,m) :
            for j in range(1,n) : 
                if matrix[i][j] == "1" : 
                    '''
                        if value is 1 : 
                            check the left, top and top left diagonal 
                            compute the min value and add 1(as it the current value)
                        compute the max of  the current node value and the Mx value
                    '''
                    x = int(matrix[i-1][j])
                    y = int(matrix[i][j-1]) 
                    z = int(matrix[i-1][j-1])
                    matrix[i][j] = str(1+min(x,y,z))
                Mx = max(int(matrix[i][j]),Mx)
        return Mx**2 # **2 as it is a square
            
            
            