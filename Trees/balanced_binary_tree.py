class Solution(object):
    def checkBalancing(self, root):
        if not root: 
            return 0
        
        left = self.checkBalancing(root.left)
        
        if left == -1: 
            return -1
        
        right = self.checkBalancing(root.right)
        
        if right == -1: 
            return -1
        
        if abs(left - right) <= 1:
            return max(left, right)+1  
        else:
            return -1
    
    
    def isBalanced(self, root):
        if self.checkBalancing(root) == -1:
            return False 
        else: 
            return True

class Solution2(object):
  def isBalanced(self, node):
    return self.isBalancedNode(node)['balanced']
  
  def isBalancedNode(self, node):
    if not node:
      return {'balanced': True, 'depth':-1}
    left = self.isBalancedNode(node.left)
    right = self.isBalancedNode(node.right)

    if left['balanced'] and right['balanced'] and abs(left['depth'] - right['depth']) <= 1:
      return {'balanced': True, 'depth': max(left['depth'],right['depth']) + 1}
    else:
      return {'balanced': False, 'depth': 0}



class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

array = [3,9,20,None,None,15,7]

for i in range(len(array)):
  if array[i]:
    array[i] = TreeNode(array[i])
for i in range(len(array)):
  if array[i]:
    node = array[i]
    if 2 * i + 1 < len(array):
      node.left = array[2 * i + 1]
    node = array[i]
    if 2 * i + 2 < len(array):
      node.right = array[2 * i + 2]
root = array[0]

obj = Solution()
obj.isBalanced(root)

obj2 = Solution2()
obj2.isBalanced(root)