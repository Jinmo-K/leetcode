class Solution:
  def maxPathSum(self, root):
    self.max = -float('inf')

    def maxNodeSum(node):
      if not node:
          return 0
      left = max(maxNodeSum(node.left), 0)
      right = max(maxNodeSum(node.right), 0)
      node_sum = node.val + left + right
      self.max = max(self.max, node_sum)
      return node.val + max(left, right)

    maxNodeSum(root)
    return self.max