class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        levels = [(root,0)]
        max_width = 1
        while levels:
            new_level = []

            
            for node in levels:
                if node[0].left:
                    new_level.append((node[0].left, node[1]*2 + 1))

                if node[0].right:
                    new_level.append((node[0].right, node[1]*2 + 2))

            levels = new_level
            if levels:
                max_width = max(max_width, new_level[-1][1] - new_level[0][1] + 1)
            
            
        return max_width





class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
# root.left.left.left = TreeNode(6)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
# root.right.right.right = TreeNode(7)


obj = Solution()
obj.widthOfBinaryTree(root)