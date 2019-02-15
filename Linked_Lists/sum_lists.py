class LinkNode:
  def __init__(self,val):
    self.val = val
    self.next = None 

root = LinkNode(7)
root.next = LinkNode(1)
root.next.next = LinkNode(6)

root2 = LinkNode(5)
root2.next = LinkNode(9)
root2.next.next = LinkNode(2)

def sumLists(l1,l2):
  str1 = ''
  str2 = ''

  while l1:
    str1 = str(l1.val) + str1 
    l1 = l1.next 
  while l2:
    str2 = str(l2.val) + str2 
    l2 = l2.next 
  
  total = int(str1) + int(str2)
  strTotal = str(total)[::-1]

  newList = LinkNode(0)
  p1 = newList

  for i in range(len(strTotal)):
    p1.next = LinkNode(int(strTotal[i]))
    p1 = p1.next 
  
  return newList.next

  

sumLists(root,root2)