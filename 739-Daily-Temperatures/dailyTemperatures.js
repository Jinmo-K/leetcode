var dailyTemperatures = function(T) {
    let stack = [];
    let ans = new Array(T.length).fill(0);
    
    for (let i = 0; i < T.length; i++) {
        while (stack.length && T[i] > T[stack[stack.length - 1]]) {
            let pos = stack.pop();
            ans[pos] = i - pos;
        }
        stack.push(i);
    }
    
    return ans;
};