class Solution:
  def findPeakElement(self, nums):
    left = 0
    right = len(nums) - 1

    while left < right:
      mid = left + (right - left) // 2
      # mid element might be a peak, so continue searching left side
      if nums[mid] > nums[mid+1]:
        right = mid
      # otherwise, continue searching on right side without including mid element
      else:
        left = mid + 1
    
    return left

