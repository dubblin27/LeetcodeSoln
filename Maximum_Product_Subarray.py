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
            