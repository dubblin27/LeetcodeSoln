# https://leetcode.com/problems/spiral-matrix/

from functools import lru_cache 
@functools.lru_cache(maxsize=128)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = [] 
        #if the length of the matrix remains to be 1 : return the first sub array 
        if len(matrix) == 1 :
            return matrix[0]
        '''
        Until the matrix has nothing in it
            pop and add the first row of the matrix to arr
            perform the zip function because 
                function of zip : 
                    it combines all the val in the same column into one single list as a whole a 2d list of columns
            then reverse it ..as it is spiral  
        '''
        while matrix : 
            arr += matrix.pop(0) 
            matrix = list(zip(*matrix))
            # print(matrix, sep="\n")
            matrix = matrix[::-1]
            # print(matrix)
        return arr
            