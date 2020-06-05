class Solution {
  public void sortColors(int[] nums) {
      int curr = 0;
      int front = 0;
      int end = nums.length - 1;
      
      while (curr <= end) {
          if (nums[curr] == 2) {
              nums[curr] = nums[end];
              nums[end] = 2;
              end--;
          }
          else {
              if (nums[curr] == 0) {
                  nums[curr] = nums[front];
                  nums[front] = 0;
                  front++;
              }
              curr++;
          }
      }
  }
}
