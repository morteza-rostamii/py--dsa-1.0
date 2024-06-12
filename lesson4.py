
import math

print('------------------------------\n')

# stack: last-in => first_out

class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    # last-in
    self.top = None
    self.size = 0

  # check if stack empty
  def is_empty(self) -> bool:
    return self.top is None
  
  # push on top
  def push(self, data):
    new_node = Node(data)

    # point to previous top
    new_node.next = self.top

    self.top = new_node
    self.size += 1

  # pop from end
  def pop(self):
    if self.is_empty():
      return None
    
    removed_node = self.top
    # previous node becomes top_node
    self.top = self.top.next
    self.size -= 1
    return removed_node
  
  # what is on the top
  def peek(self):
    if self.is_empty():
      return None
    
    return self.top
  
  # print stack
  def __str__(self):
    current_node = self.top
    items = []

    while current_node:
      items.append(str(current_node.data))
      current_node = current_node.next

    return ' - '.join(items) if items else "Empty Stack"

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
#print(stack1.pop().data)

#print(stack1)

#=========================================

# Queue: first in => first out -> shop's line

class Queue:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return len(self.items) == 0

  def enqueue(self, item):
    # append to the end
    self.items.append(item)

  # fist out
  def dequeue(self):

    if self.isEmpty():
      raise IndexError('Queue is empty')
    # remove & return first element
    return self.items.pop(0)

  def size(self):
    return len(self.items)

queue1 = Queue()
queue1.enqueue('love')
queue1.enqueue('apple')

print(queue1.dequeue())
print(queue1.items)

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
#=========================================
#=========================================
#=========================================


print('\n------------------------------')