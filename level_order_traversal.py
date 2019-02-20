class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    output = [[root.val]]
    level = [root]
    while level:
        new_level = []
        for node in level:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        temp = []
        for node in new_level:
            temp.append(node.val)
        if temp:
          output.append(temp)
        level = new_level
    return output

levelOrder(root)