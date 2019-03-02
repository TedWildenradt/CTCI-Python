class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
arr = [2]
headNode = LinkNode(1)
curr = headNode 
for i in arr:
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 

obj = Solution()
obj.removeNthFromEnd(headNode,2)