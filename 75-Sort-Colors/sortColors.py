class Solution:
  def sortColors(self, nums):
    curr, front, end = 0, 0, len(nums) - 1
    
    while curr <= end:
        if nums[curr] == 2:
            nums[curr], nums[end] = nums[end], nums[curr]
            end -= 1
        else:
            if nums[curr] == 0:
                nums[curr], nums[front] = nums[front], nums[curr]
                front += 1
            curr += 1
