def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    dummyHead = LinkNode(0)
    dummyHead.next = head
    
    curr = head
    i = 1
    if m > 1:
      while i < m:
          start = curr
          curr = curr.next
          i += 1
    else:
      start = dummyHead
        
    prev = None
    end = curr
    
    while i <= n:
        after = curr.next
        curr.next = prev
        prev = curr
        curr = after
        i += 1
        
    start.next = prev
    end.next = curr

    check = dummyHead.next
    while check:
      print(check.val)
      check = check.next

    return dummyHead.next



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

reverseBetween(headNode,3,5)