# https://leetcode.com/problems/contiguous-array/submissions/
# Ref Soln : https://www.youtube.com/watch?v=9ZyLjjk536U&t=654s

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2 : return 0 
        Sum = 0 
        Max = 0 
        HashMap = {} 
        
        for i in range(len(nums)) : 
            if nums[i] == 0 : 
                Sum -= 1
            else:
                Sum +=1 
            
            if Sum ==0 : 
                Max = i + 1
            elif Sum not in HashMap : 
                HashMap[Sum] = i 
            else : 
                Max = max(Max, i - HashMap[Sum])
        
        return Max