class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            
            # Since area is constrained by the shorter side, keep the longer side
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return ans