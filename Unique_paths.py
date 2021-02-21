class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for i in range(m)] # initialize the matrix
        # set all the last row and column as 1 
        matrix[-1] = [1]*n 
        for i in range(m-1) : 
            matrix[i][-1] = 1 
        '''
        for each node from diag of end node : 
            compute the sum  of down and right 
            until the initial matrix[0][0]
        '''
        for i in range(m-2,-1,-1) : 
            for j in range(n-2,-1,-1) : 
                # print(i,j)
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]
            