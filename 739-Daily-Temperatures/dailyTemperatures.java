class Solution {
    public int[] dailyTemperatures(int[] T) {
        Stack<Integer> stack = new Stack<Integer>();
        int[] ans = new int[T.length];
        
        for (int i = 0; i < T.length; i++) {
            while (!stack.isEmpty() && T[i] > T[stack.peek()]) {
                int pos = stack.pop();
                ans[pos] = i - pos;
            }
            stack.push(i);
        }
        
        return ans;
    }
}