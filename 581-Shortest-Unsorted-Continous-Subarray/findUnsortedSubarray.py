class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_num = float('-inf')
        min_num = float('inf')
        sort_start = 0
        sort_end = -1
        
        for r in range(len(nums)):
            l = ~r
            
            if nums[l] <= min_num:
                min_num = nums[l]
            else:
                sort_start = l + len(nums)
                
            if nums[r] >= max_num:
                max_num = nums[r]
            else:
                sort_end = r
                
        return sort_end - sort_start + 1