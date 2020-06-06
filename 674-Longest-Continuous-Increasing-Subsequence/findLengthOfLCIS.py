class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        max_length = 1
        curr_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_length += 1
            else:
                curr_length = 1
            max_length = max(max_length, curr_length)
        
        return max_length