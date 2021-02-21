# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
from functools import lru_cache 
@functools.lru_cache(maxsize=128)
class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums : return None 
        res = max(nums) 
        minV = 1 
        maxV = 1 
        
        for n in nums : 
            if n == 0 : 
                minV, maxV = 1, 1 
                continue 
            tmp = n*maxV
            maxV = max(n, n*minV,n*maxV)
            minV = min(n, n*minV,tmp)
            res = max(res,maxV)
        return res
        
        '''
            finding the min value and the max value and storing them
            multiplying them with the the i'th term of the array and 
            again calculating the max and the min value and again storing them
            storing the max in the result 

            for eg [2,-2,0,3] 
            minV, maxV = 1,1 
            maxV = (2,2*1,2*1) = 2 
            minV = (2,2*1,2*1) = 2 
            res = 2 

            minV, maxV = 2,2
            maxV = (-2,-4,-4) = -2
            minV = (-2,-4,-4) = -2
            res = 2 

            minV,maxV = -2,-2 
            minvV, maxV = 1,1 
            res = 2

            minV,maxV = 1,1
            maxV = (3,3,3)
            minV = (3,3,3) 
            res = 3 

            return res = 3
        '''