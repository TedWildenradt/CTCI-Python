class Node:
  def __init__(self,k,v):
    self.key = k 
    self.val = v
    self.prev = None
    self.next = None 

class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.hash = {}
    self.tail = Node(0,0)
    self.head = Node(0,0)
    self.tail.prev = self.head
    self.head.next = self.tail 

  def _remove(self, node):
    n = node.next
    p = node.prev
    n.prev = p
    p.next = n 

  def _add(self, node):
    p = self.tail.prev
    p.next = node 
    node.prev = p
    node.next = self.tail
    self.tail.prev = node 

  def get(self,key):
    if key in self.hash:
      n = self.hash[key]
      self._remove(n)
      self._add(n)
      return n.val
    else:
      return -1

  def put(self,key,value):
    if key in self.hash:
      self._remove(self.hash[key])
    newNode = Node(key,value)
    self._add(newNode)
    self.hash[key] = newNode
    if len(self.hash) > self.capacity:
      oldNode = self.head.next 
      self._remove(oldNode)
      del self.hash[oldNode.key]
  

