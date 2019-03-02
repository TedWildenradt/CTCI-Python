class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        fast = slow = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next           
        prev.next = None
        
        right = self.mergeSort(slow)
        left = self.mergeSort(head)
        return self.merge(left,right)
        
        
        
        
    def merge(self,left, right):
        dummy = dummyHead = LinkNode(0)
        while left and right:
            if left.val < right.val:
                dummy.next = left
                left = left.next 
            else:
                dummy.next = right
                right = right.next 
            dummy = dummy.next 
        if left:
            dummy.next = left 
        else:
            dummy.next = right
        return dummyHead.next


obj = Solution()

class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
arr = [5,3,4,0]
headNode = LinkNode(-1)
curr = headNode 
for i in arr:
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 

x = obj.mergeSort(headNode)
while x:
  print(x.val)
  x = x.next