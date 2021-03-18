class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums : return 0
        if len(nums) < 3: 
            return max(nums)
        
        nums1 = nums[:-1]
        if len(nums1) < 3 : return max(nums1)
        a = nums1[0]
        b = max(nums1[0],nums1[1])
        for i in range(2,len(nums1)) : 
            Curr_max = max(a+nums1[i], b)
            a = b 
            b = Curr_max 
        
        nums2 = nums[1:]
        # if not nums2 : return 0
        if len(nums2) < 3 : return max(nums2)
        c = nums2[0]
        d = max(nums2[0],nums2[1])
        for i in range(2,len(nums2)) : 
            Curr_max = max(c+nums2[i], d)
            c = d 
            d = Curr_max 
        return max(b,d)
        
        
        