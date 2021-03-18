# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = [] 
        nums = sorted(nums) 
        n = len(nums) 
        
        for i in range(n) : 
            start = i + 1
            end = n -1
            
            while start < end : 
                Sum = nums[i] + nums[start] + nums[end] 
                
                if Sum > 0 : 
                    end -= 1
                elif Sum < 0 : 
                    start +=1 
                else :
                    arr.append((nums[i], nums[start],nums[end]))
                    start +=1 
                    end -= 1 
        return list(set(arr))
