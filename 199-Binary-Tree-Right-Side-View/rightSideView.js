var rightSideView = function(root) {
    let ans = [];

    const dfs = (node, level) => {
        if (node) {
            if (level === ans.length) {
                ans.push(node.val);
            }
            dfs(node.right, level + 1);
            dfs(node.left, level + 1);
        }
    };
    
    dfs(root, 0);
    return ans;
};