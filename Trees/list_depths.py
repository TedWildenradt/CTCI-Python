class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

