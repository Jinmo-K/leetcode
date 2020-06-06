class Solution {
  int max_sum;
  
  public int maxPathSum(TreeNode root) {
    max_sum = Integer.MIN_VALUE;
    maxNodeSum(root);
    return max_sum;
  }
  
  private int maxNodeSum(TreeNode node) {
    if (node == null) {
      return 0;
    }
    
    int left = Math.max(maxNodeSum(node.left), 0);
    int right = Math.max(maxNodeSum(node.right), 0);
    int node_sum = node.val + left + right;
    max_sum = Math.max(max_sum, node_sum);
    return node.val + Math.max(left, right);
  }
}