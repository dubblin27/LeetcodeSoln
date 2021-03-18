class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        2
        3 4
        6 5 7 
        4 1 8 3
        '''
        if not triangle : return 0
        if len(triangle) == 1: return triangle[0][0] 
        n = len(triangle) 
        
        for i in range(n-2,-1,-1) : 
            for j in range(len(triangle[i])) : 
                # start with 2nd last sub array then find the min of (current element + down element and current element+ right down diag element )
                # replace it with the min of those 2
                triangle[i][j] = min((triangle[i][j]+triangle[i+1][j]),(triangle[i][j]+triangle[i+1][j+1]))
        return triangle[0][0]
            
        