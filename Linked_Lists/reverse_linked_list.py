class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head)
    def reverse(self,node,prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n,node)

class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
arr = [2,3,4,5]
headNode = LinkNode(1)
curr = headNode 
for i in arr:
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 

obj = Solution()
obj.reverseList(headNode)