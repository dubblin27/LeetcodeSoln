# https://leetcode.com/problems/trapping-rain-water/ 

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0 : return 0 
        l,r = [0]*n,[0]*n  
        
        l[0] = height[0]
        for i in range(1,n) : 
            l[i] = max(l[i-1],height[i])
        
        hx = height[::-1] 
        r[0] = hx[0] 
        for i in range(1,n):
            r[i] = max(r[i-1],hx[i])
        r= r[::-1]
        c = 0
        for i in range(n):
            c += min(l[i],r[i]) - height[i]
        return c