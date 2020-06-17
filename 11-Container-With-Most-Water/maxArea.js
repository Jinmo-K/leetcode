var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let ans = 0;
    
    while (left < right) {
        let area = Math.min(height[left], height[right]) * (right - left);
        ans = Math.max(ans, area);
        
        if (height[left] > height[right]) {
            right--;
        }
        else {
            left++;
        }
    }
    
    return ans;
};