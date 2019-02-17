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

def list_of_depths(root):
  if not root:
    return None
  output = [LinkNode(root.val)]
  level = [root]
  while level:
    new_level = []
    for node in level:
      if node.left:
        new_level.append(node.left)
      if node.right:
        new_level.append(node.right)
    head = LinkNode(0)
    curr = head 
    for node in new_level:
      link = LinkNode(node.val)
      curr.next = link 
      curr = curr.next 
    output.append(head.next)
    level = new_level
  return output[:-1] 

list_of_depths(root)
