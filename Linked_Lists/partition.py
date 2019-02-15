class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
arr = [5,8,5,10,2,1]
headNode = LinkNode(3)
curr = headNode 
for i in arr:
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 

def partition(head, k):
  leftRoot = LinkNode(0)
  currLeft = leftRoot

  rightRoot = LinkNode(0) 
  currRight = rightRoot 

  curr = head 
  while curr:
    if curr.val < k:
      currLeft.next = curr 
      currLeft = currLeft.next 
    else: 
      currRight.next = curr 
      currRight = currRight.next 
    curr = curr.next 
  currRight.next = None
  currLeft.next = rightRoot.next 
  return leftRoot.next 

x = partition(headNode, 5)

