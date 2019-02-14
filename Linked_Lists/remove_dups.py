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


def remove_dups(head):
  visited = set()
  p1 = head 
  prev = None
  while p1:
    if p1.val in visited:
      prev.next = p1.next
      p1 = p1.next
    else:
      visited.add(p1.val) 
      prev = p1 
      p1 = p1.next
  return head 

remove_dups(headNode)

