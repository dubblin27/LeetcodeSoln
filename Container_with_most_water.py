# https://leetcode.com/problems/container-with-most-water/ 
#Optimized
class Solution:
    def maxArea(self, height: List[int]) -> int:
        x = 0
        n = len(height)
        y = n-1 
        arr = []
        for i in range(len(height)) : 
            if height[x]>height[y]:
                
                arr.append(height[y]*(y-x))
                y-=1 
            elif height[x]<height[y]:
                arr.append(height[x]*(y-x))
                x+=1 
            else:
                arr.append(height[x]*(y-x))
                x+=1
            
        return max(arr)
                    
        
        