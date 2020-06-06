class Solution {
  public int findLengthOfLCIS(int[] nums) {
    int max_length = 0;
    int curr_length = 0;

    for (int i = 0; i < nums.length; i++) {
      curr_length++;
      if (i > 0 && nums[i] <= nums[i-1]) {
        curr_length = 1;
      }
      max_length = Math.max(max_length, curr_length);
    }

    return max_length;
  }
}