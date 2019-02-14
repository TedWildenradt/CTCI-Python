class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
arr = [2,2,4,4,5,6]
headNode = LinkNode(1)
curr = headNode 
for i in arr:
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 

def kth_to_last(head, k):
  p1 = head 
  p2 = head 
  i = 0

  while i < k:
    p2 = p2.next 
    i += 1

  while p2:
    p1 = p1.next 
    p2 = p2.next 
  return p1.val

kth_to_last(headNode, 3)
