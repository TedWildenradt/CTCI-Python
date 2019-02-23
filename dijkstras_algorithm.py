import collections

class Graph:
  def __init__(self):
    """
    self.edges is a dict of all possible next nodes
    e.g. {'X': ['A', 'B', 'C', 'E'], ...}
    self.weights has all the weights between two nodes,
    with the two nodes as a tuple as the key
    e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
    """
    self.edges = collections.defaultdict(list)
    self.weights = {}

  def add_edge(self, from_node, to_node, weight):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.weights[(from_node, to_node)] = weight
    self.weights[(to_node, from_node)] = weight

graph = Graph()
edges = [
  ('X', 'A', 7),
  ('X', 'B', 2),
  ('X', 'C', 3),
  ('X', 'E', 4),
  ('A', 'B', 3),
  ('A', 'D', 4),
  ('B', 'D', 4),
  ('B', 'H', 5),
  ('C', 'L', 2),
  ('D', 'F', 1),
  ('F', 'H', 3),
  ('G', 'H', 2),
  ('G', 'Y', 2),
  ('I', 'J', 6),
  ('I', 'K', 4),
  ('I', 'L', 4),
  ('J', 'L', 1),
  ('K', 'Y', 5)]

for edge in edges:
  graph.add_edge(*edge)


def dijkstra(graph, initial, end):
  shortest_paths = {initial: (None, 0)}
  current_node = initial
  visited = set()
  
