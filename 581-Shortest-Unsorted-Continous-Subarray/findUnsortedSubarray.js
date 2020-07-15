/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {
  let max_num = -Infinity;
  let min_num = Infinity;
  let sort_start = 0;
  let sort_end = -1;
  let right = 0;
  let left = nums.length - 1;
  
  while (left >= 0) {
      nums[left] <= min_num ? min_num = nums[left] : sort_start = left;
      nums[right] >= max_num ? max_num = nums[right] : sort_end = right;
      right++;
      left--;
  }
  
  return sort_end - sort_start + 1;
};