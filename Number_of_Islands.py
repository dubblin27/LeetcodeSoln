# https://leetcode.com/problems/number-of-islands/
@functools.lru_cache(maxsize=None)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid,i,j) : 
            if i<0 or i > len(grid)-1 or j <0 or j > len(grid[0]) -1 or grid[i][j] == '0' or grid[i][j] == '2' or (i,j) in visited : 
                return 0
            visited.add((i,j))
            dfs(grid,i-1,j)
            dfs(grid,i+1,j)
            dfs(grid,i,j-1)
            dfs(grid,i,j+1)
            grid[i][j] = "2"
            
            return 1      
                    
                    
        count = 0
        visited = set()
        for i in range(len(grid))  : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == "1" :
                    count += dfs(grid,i,j)
        return count
                