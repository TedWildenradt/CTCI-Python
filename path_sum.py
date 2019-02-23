def pathSum(root, s):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    counter = 0
    def inorder(root,total):
        if not root:
            return 
        total += root.val
        if total == s:
            counter += 1
        inorder(root.left,total)
        inorder(root.right,total)
        
    inorder(root,0)
    return counter

class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

pathSum(root,8)
