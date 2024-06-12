
import math

print('------------------------------\n')

"""
# graph => nodes => edges

# edge: connection between nodes.
# a -> b -> c

# directed graph =: arrow head on edges
  # only can go to direction of arrow
# undirected graph => no arrow head
  # no direction

# neighbor node: 
  # b and c are neighbors of a , meaning from a you can only directly go to either b or c.
  
a -> b
|
v
c
  
# adjacency list: 
  # Object, dic or hash map.

graph: {
  a: {
    value: 1,
    edges: [b, c]
  },
  b: {
    value: 2,
    edges: []
  },
  c: {
    value: 3,
    edges: [],
  }
}

"""

# class Node:
#   def __init__(self, value) -> None:
#     self.value = value

#   def 

# graph (using dic)
class Graph:

  def __init__(self):
    # all the nodes
    self.nodes = {}

  # add: node: a: {value: , edges: }
  def add_node(self, key, val):
    self.nodes[key] = {
      'value': val,
      'edges': [],
    }
  
  # add edge between nodes
  def add_edge(self, n1_key: str, n2_key: str):
    # raise error if: one node does not exist
    if n1_key not in self.nodes or n2_key not in self.nodes:
      raise ValueError("Nodes not found in the graph.")
    
    self.nodes[n1_key]['edges'].append(n2_key)

  def get_neighbors_by_key(self, key):
    if key not in self.nodes:
      raise ValueError("Node not found in the graph")
    return self.nodes[key]['edges']

  def get_node_by_value(self, val):
    for node in self.nodes:
      if node.value == val:
        return node

  def get_node_by_key(self, key):
    return self.nodes[key]

# create a graph
graph1 = Graph()
graph1.add_node('a', 11)
graph1.add_node('b', 12)
graph1.add_node('c', 13)

# setup edges
graph1.add_edge('a', 'b')
graph1.add_edge('a', 'c')

#print(graph1.get_neighbors_by_key('a'))
#print(graph1.get_neighbors_by_key('b'))

#-------------------------------------

graph2 = Graph()
graph2.add_node('a', 'a')
graph2.add_node('b', 'b')
graph2.add_node('c', 'c')
graph2.add_node('d', 'd')
graph2.add_node('e', 'e')
graph2.add_node('f', 'f')

graph2.add_edge('a', 'b')
graph2.add_edge('a', 'c')
graph2.add_edge('b', 'd')
graph2.add_edge('c', 'e')
graph2.add_edge('d', 'f')

# depth first traversal:

def depth_first_traversal(graph, start_node:str):
  stack = []
  # keep track of visited nodes
  visited = set()

  # starting random node
  current_node = start_node

  # push first node into stack
  stack.append(current_node)

  while len(stack):
    # pop last in element
    current_node = stack.pop()

    # check if node is not visited
    if current_node not in visited:
      # add node to visited
      visited.add(current_node)
      
      node_obj = graph.get_node_by_key(current_node)
      print(node_obj)

      # pop neighbors
      while len(node_obj['edges']):
        # if: a: [b, c] => push: c & b onto stack on that order
        stack.append(node_obj['edges'].pop())
    else:
      # just to see in which case we go to a already visited node.
      print('visited: ', current_node)

#depth_first_traversal(graph2, 'a')

# breadth first traversal
def breadth_first_traversal(graph, first_node:str):
  queue = []

  current_node = first_node

  queue.append(current_node)

  while len(queue):
    current_node = queue.pop(0)

    node_obj = graph.get_node_by_key(current_node)
    print(node_obj)

    while len(node_obj['edges']):
      queue.append(node_obj['edges'].pop(0))
  
#breadth_first_traversal(graph2, 'a')

#=========================================

"""
# acyclic = no cycles graph
  # there is no infinite cycle that you ca start from node a and end up on node a in a cycle.

f -> g -> h
|  .
v /
i  <- j
|
v
k

# source_node & destination_node

# can we travel from src_node to dst_node?
  # is there a path?

"""

my_graph = {
  "f": ["g", "i"],
  "g": ["h"],
  "h": [],
  "i": ["g", "k"],
  "j": ["i"],
  "k": [],
}

# using depth-first-search
def is_there_a_path(graph, src, dst):
  # if: src === dst
  if src == dst: 
    return True
  
  stack = []

  current_node = src
  stack.append(current_node)

  while len(stack):
    current_node = stack.pop()

    # if: we started with src and now on dst =: there is a path
    if current_node == dst:
      return True
    
    # list of neighbors
    while len(graph[current_node]):
      node = graph[current_node].pop()
      stack.append(node)
    
  return False

src = 'f'
dst = 'k'

found_path = is_there_a_path(my_graph, src, dst)
#print(F"path to: {src} - {dst}", found_path)

#=========================================

# undirected graph path problem:
# i to j and j to i => it's two ways.

# if: there is an edge it's two ways.
  # i -> j and j -> i

"""

# e = number of edges
# time complexity: O(e)
  # for each arrow-head we loop once

# n = number of nodes 
# space complexity: O(n)
  # we push each node onto the stack
    # even if there is no edge to this node from other nodes.
"""

graph3 = {
  "i": ['j', 'k'],
  "j": ['i'],
  "k": ['i', 'm', 'l'],
  "m": ['k'],
  "l": ['k'],
  "o": ['n'],
  "n": ['o'],
}

# breadth-first search
def find_path(graph, src, dst):
  if src == dst:
    return True
  
  queue = []
  # store visited nodes
  visited = set()

  current_node = src
  queue.append(current_node)
  #visited.add(current_node)
  
  while len(queue):
    current_node = queue.pop(0)

    # if: we have visited this node before, it means: we also pushed it's neighbors onto the queue
    if current_node not in visited: 
      print(current_node, current_node not in visited)
      visited.add(current_node)

      #print(current_node)

      # check: if there is a path
      if current_node == dst:
        return True

      # get neighbors
      while len(graph[current_node]):
        node = graph[current_node].pop(0)
        queue.append(node)

  return False

src = 'i'
dst = 'k'

#res = find_path(graph3, src, dst)
#print(F"result: {res}")

#=========================================

"""
# connected components count:

# 

"""

undirected1 = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1],
}

# depth-first
def visit_connected(graph, start_node:str, visited):
  # if: the node already visited return 0
  # we already been in this component
  if start_node in visited:
    return 0
    
  count = 0
  stack = []

  current_node = start_node
  stack.append(current_node)

  while len(stack):
    current_node = stack.pop()
    
    if current_node not in visited:
      # the goal was to set the visited nodes => this way we don't count components again
      visited.add(current_node)

      while len(graph[current_node]):
        n = graph[current_node].pop()
        stack.append(n)

  # at the end of traversing all nodes in a component =: increment the count
  count += 1
  return count

# component: means a set of connected nodes.
def count_connected_components(graph):
  # component count
  count = 0
  # visited nodes
  visited = set()

  # loop the whole graph_nodes
  for node in undirected1:
    # returns 1 on each component visit
    res = visit_connected(graph, node, visited)
    count += res

  return count

components_count = count_connected_components(undirected1)
print(components_count)

#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================


print('\n------------------------------')