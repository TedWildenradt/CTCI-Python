class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(root):
            if root:
                data.append(str(root.val))
                traverse(root.left)
                traverse(root.right)
            else:
                data.append('#')
        data = []
        traverse(root)
        return ' '.join(data)
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build():
            val = array.next()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        array = iter(data.split())
        return build()


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(1)

codec = Codec()
data = codec.serialize(root)
codec.deserialize(data)
