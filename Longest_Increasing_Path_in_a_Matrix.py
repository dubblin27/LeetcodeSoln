
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
from functools import lru_cache 

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def neighbours(i,j):
            #just incrementing to find top down left right values
            
            arr = []
            
            if i> 0 :
                arr.append((i-1, j))
            if i < L-1 :
                arr.append((i+1, j))
            if j > 0 :
                arr.append((i, j-1))
            if j < M-1 : 
                arr.append((i, j+1))
            
            return arr
        
        def long_path(i,j) : 
            #for each value the Max is initialized to 1
            # after that max is found using recursion
            Max = 1 
            for x,y in neighbours(i,j):
                if matrix[x][y] > matrix[i][j]:
                    # if there is a greater value then do this 
                    Max = max(Max,long_path(x,y)+1)
            return Max
        
        if not matrix : return 0 
        L = len(matrix) 
        M = len(matrix[0])
        
        Max = 1 
        for i in range(L) : 
            for j in range(M) : 
                Max = max(Max,long_path(i,j))
        return Max
        