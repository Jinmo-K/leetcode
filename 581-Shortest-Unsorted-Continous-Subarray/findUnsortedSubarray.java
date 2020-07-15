class Solution {
  public int findUnsortedSubarray(int[] nums) {
      int max = Integer.MIN_VALUE;
      int min = Integer.MAX_VALUE;
      int start = 0;
      int end = -1;
      int right = 0;
      int left = nums.length - 1;
      
      while (left >= 0) {
          if (nums[left] <= min) {
              min = nums[left]; 
          } else {
              start = left;
          }
          if (nums[right] >= max) {
              max = nums[right];
          } else {
              end = right;
          }
          left--;
          right++;
      }
      
      return end - start + 1;
  }
}