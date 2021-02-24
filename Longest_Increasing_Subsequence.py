from bisect import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [] 
        for i in range(len(nums)) : 
            '''
                Bisect_left returns:
                    1. where the value should be placed according to increasing order of array
                    2. if value already in .. it shows the idx of the value 
                    3. if val not it shows the len(arr) which is 1 + the idx of the last value
            '''
            idx = bisect_left(dp,nums[i])
            if idx == len(dp) : 
                dp += [nums[i]]
            else:
                dp[idx] = nums[i] 
        return len(dp)