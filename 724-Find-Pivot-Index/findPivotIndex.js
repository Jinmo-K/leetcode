/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let total_sum = nums.reduce((a, b) => a + b);
    let left_sum = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (total_sum - nums[i] - left_sum === left_sum) {
            return i;
        }
        left_sum += nums[i];
    }
    return -1;
};