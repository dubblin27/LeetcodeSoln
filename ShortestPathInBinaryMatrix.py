https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        M = len(grid) 
        N = len(grid[0]) 
        visited = set()
        q = deque()
        dirs = [(1,0),(-1,0),(0,-1),(0,+1),(-1,-1),(1,1),(-1,1),(1,-1)]
        
        if grid[0][0] == 0 :
            q.append((1,(0,0))) 
            visited.add((0,0))
        
        while q :
            steps,temp = q.popleft()
            r,c = temp[0],temp[1] 
            
            if (r,c) == (M-1,N-1):
                return steps 
            
            for i,j in dirs: 
                nR, nC = i+r, j+c 
                
                if 0<=nR<M and 0<= nC < N and grid[nR][nC] == 0 and (nR,nC) not in visited:
                    q.append((steps+1,(nR,nC))) 
                    visited.add((nR,nC))
        return -1

#2 

import heapq
@functools.lru_cache(maxsize = None)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = []
        heapq.heapify(res) 
        visited = set()
        heappush(res,(1,0,0))

        if grid[0][0] == 1 : 
            return -1
        while res:
            # print("in")
            diff,x,y = heappop(res) 
            if (x,y) in visited:
                continue
            elif (x,y) == (R-1,C-1) :
                return diff 
            visited.add((x,y))
            # print(x,y)
            for (i,j) in((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)) :
                # print(i,j," i j")
                x1,y1 = x+i, y+j

                if 0 <= x1 < R and 0<= y1 < C and (x1,y1) not in visited and grid[x1][y1] == 0 :
                    # print("iij")
                    heappush(res,(diff+1,x1,y1))
                    # print(res)
                    # visited.add((x1,y1))
        return -1