# https://leetcode.com/problems/max-consecutive-ones-iii/ 
# used sliding window
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = 0 
        while end < len(A) : 
            if A[end] == 0 : 
                K -=1 
            
            if K < 0 : 
                if A[start] == 0 :
                    K +=1
                start+=1
            end+=1
        return end - start