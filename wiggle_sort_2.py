# https://leetcode.com/problems/wiggle-sort-ii/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums = sorted(nums)
        for i in range(0,len(nums),2) : 
            if len(nums[i:]) == 1:
                break
            nums[i:] = [nums[i]] + [nums[-1]] + nums[i+1:-1] 
        print(nums)