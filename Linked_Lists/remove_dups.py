class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
headNode = LinkNode(1)
curr = headNode 
i = 2
for i in range(2,7):
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 
  node = LinkNode(i*2)
  curr.next = node
  curr = curr.next
