class Solution:
  def univalSubTrees(self, root):
    if not root:
      return 0
    self.output = 0

    def traverse(root):
      if not root:
        return True
      left = traverse(root.left)
      right = traverse(root.right)
      if (root.left == None or root.left.val == root.val) and (root.right == None or root.right.val == root.val) and left and right:
        self.output += 1
        return True 
      else:
        return False
    traverse(root)
    return self.output
    
    




class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)

obj = Solution()
obj.univalSubTrees(root)