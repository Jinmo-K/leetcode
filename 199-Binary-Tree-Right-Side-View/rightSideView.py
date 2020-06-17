class Solution:
  def rightSideView(self, root):
    ans = []

    def dfs(node, level):
      if not node:
        return
      # len(ans) is the minimum point at which the node is not being 'blocked'
      # by other nodes on its right 
      if level == len(ans):
        ans.append(node.val)
      dfs(node.right, level + 1)
      dfs(node.left, level + 1)
    
    dfs(root, 0)
    return ans