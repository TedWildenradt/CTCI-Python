class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 
arr = ['b','c','d','e','f']
headNode = LinkNode('a')
curr = headNode 
for i in arr:
  node = LinkNode(i)
  curr.next = node 
  curr = curr.next 
middle = headNode
for i in range(2):
  middle = middle.next 

def remove_middle_node(node):
  p1 = node 
  while p1.next.next:
    p1.val = p1.next.val 
    p1 = p1.next 
  p1.val = p1.next.val
  p1.next = None 

remove_middle_node(middle)

  
