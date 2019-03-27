class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
          return head
        curr, length = head, 0

        while curr:
          length += 1
          curr = curr.next
        
        k %= length

        if k == 0:
          return head 
        
        fast = slow = head
        for i in range(k):
          fast = fast.next
        
        while fast and fast.next:
          fast = fast.next
          slow = slow.next
        
        output = slow.next
        fast.next = head
        slow.next = None
        return output

head = ListNode(1)
curr = head
for i in range(2,6):
  curr.next = ListNode(i)
  curr = curr.next

obj = Solution()
obj.rotateRight(head, 2)