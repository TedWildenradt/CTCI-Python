def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    stack = [root]
    output = []
    while stack:
        curr = stack.pop()
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
        output.append(curr.val)
    return output[::-1]

class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

postorderTraversal(root)