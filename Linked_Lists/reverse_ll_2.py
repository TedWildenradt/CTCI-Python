def reverseLL(head,m,n):
  if m - n == 0:
    return head
  
  prev = None
  curr = head
  i = 1
  while i != m:
      prev = curr
      curr = curr.next
      i += 1
  end = prev
  after = curr.next
  prev = None
  
  while i <= n:
      curr.next = prev
      prev = curr
      curr = after
      if after:
        after = after.next
      i += 1
  if not end:
    newHead = prev
    while prev.next:
      prev = prev.next
    prev.next = curr
    return newHead
  else:  
    tail = end.next
    end.next = prev
    tail.next = curr
    return head





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

reverseLL(headNode,1,3)