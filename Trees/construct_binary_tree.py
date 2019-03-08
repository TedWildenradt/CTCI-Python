def buildTree(preorder, inorder):
  if not preorder:
    return None

  node = TreeNode(preorder[0])
  i = inorder.index(preorder[0])
  node.left = buildTree(preorder[1:i+1], inorder[:i])
  node.left = buildTree(preorder[i+1:], inorder[i+1:])

  return node 


class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

buildTree(preorder,inorder)
'''
1)  first node of preorder is root node
2)  finding the root val on the inorder traversal shows where to split the left and right side of the tree
3)  there is a middle splitting point in the preorder traversal as well considering the entire left side is traversed before jumping to the right side
4)  the number of values to take from the preorder array for the left side would be the same as the number of values taken for the left side from the inorder traversal. the only difference being that in the preorder array you take away the first value, and in the inorder array you take the value at the index where it matches the first preorder value
'''