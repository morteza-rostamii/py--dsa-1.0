
import math

print('------------------------------\n')

# liked list 

class Node: 
  def __init__(self, data=None):
    self.data = data
    self.next = None

class SinglyLinkedList:

  def __init__(self):
    # the first node in our list
    self.head = None
    self.tail = None
    # length
    self.size = 0

  # push to the end
  def append(self, data):
    self.size += 1
    new_node = Node(data)

    # if head is empty
    if self.head is None:
      self.head = new_node
      return
    
    # starting with head =: we move to the last none
    current_node = self.head
    # last_node.next = None =: so: last current_node in the loop is the last node
    while current_node.next:
      # get the next node in each loop
      current_node = current_node.next
    
    # new_node.next = None
    current_node.next = new_node

    self.tail = new_node

  # pop the last element
  def pop(self):
    current_node = self.head
    prev_node = None

    # if list is empty
    if current_node == None:
      return None

    while current_node.next:
      prev_node = current_node
      current_node = current_node.next
    
    prev_node.next = None
    # set the tail
    self.tail = prev_node 
    self.size -= 1
    return current_node
  

  # push to the front of the list
  def prepend(self, data):
    self.size += 1
    new_node = Node(data)

    # new_node -> previous_head
    new_node.next = self.head
    # new_node is: the new_head
    self.head = new_node

    # if: tail is the head (one node)
    if self.head == self.tail:
      self.tail = new_node

  # insert a new node after a given node
  def insert_after(self, prev_node, data):
    if prev_node is None:
      print('The given previous node cannot be None')
      return

    self.size += 1
    new_node = Node(data)
    # a -> b => new_node.next -> a.next
    new_node.next = prev_node.next

    # set new_node as tail
    if prev_node.next == None:
      self.tail = new_node 

    # a -> new_node
    prev_node.next = new_node


  # find node
  def find_node(self, key):

    current_node = self.head

    # if head is empty
    if current_node is None:
      return

    # find node
    while current_node is not None and current_node.data != key:
      current_node = current_node.next

    # if: not found return None
    return current_node     

  # delete
  def delete_node(self, key):

    current_node = self.head
    # a -> b -> c =: we remove b and connect a -> c
    prev_node = None

    # if: list is empty
    if current_node == None:
      return
    
    # if: element is found on the head
    if current_node.data == key:
      self.head = current_node.next
      current_node = None
      return

    # loop from head to the target node
    # until: reach the last one with .next = None
    while current_node is not None and current_node.data != key:
      prev_node = current_node
      current_node = current_node.next

    # if we reach the end and could not find the item
    if current_node is None:
      return
    
    # if: we are removing the tail
    if current_node == self.tail:
      self.tail = prev_node

    # if: we found the node =: remove
    prev_node.next = current_node.next
    # remove current
    current_node = None


    # decrement the size
    self.size -= 1
  
  def reverse(self):
    
    # keep original head, to set tail at the end
    original_head = self.head

    prev = None
    current = self.head
    next = None

    # [1, 2, 3]
    # prev=None current=1 next=2 => prev=1 current=2 next=3
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next

    self.head = prev
    self.tail = original_head

    # if: only one element
    if self.tail is None:
      self.tail = self.head

  # print a list of all values
  def print_list(self):
    current_node = self.head

    while current_node:
      print(F"{current_node.data}", end=" ")
      current_node = current_node.next
    
    #print('----')

first_list = SinglyLinkedList()
first_list.append(1)
first_list.append(13)
first_list.append(14)

first_list.prepend('ali')
last = first_list.pop()
#print(last.data)

node = first_list.find_node(13)
first_list.insert_after(node, 56)

first_list.delete_node(56)

#print('Head:', first_list.head.data)
#print('List Size: ', first_list.size)
#print('Tail:', first_list.tail.data)

first_list.reverse()

#first_list.print_list()

#=========================================

# Doubly linked list

class Node2:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # push to the end
  def push(self, data):
    # create a new Node
    new_node = Node2(data)

    # if: list empty 
    if self.size == 0:
      self.head = new_node
      self.tail = self.head
      self.size += 1
      return

    # if: list has 1 element
    # if self.size == 1:
    #   new_node.prev = self.tail
    #   self.tail.next = new_node

    # at least one element
    self.tail.next = new_node
    new_node.prev = self.tail
    self.tail = new_node

    self.size += 1

  # pop the last item
  def pop(self):
    temp = self.tail

    # if: list empty
    if self.size == 0:
      return None
    
    # if: one item
    if self.size == 1:
      self.head = None
      self.tail = None
      self.size -= 1
      return temp.data

    # list not empty
    prev = self.tail.prev
    prev.next = None
    self.tail = prev

    self.size -= 1
    # return last item
    return temp.data

  # shift: remove element from the beginning
  def shift(self):
    removed = self.head
    
    # list is empty 
    if self.size == 0:
      return None
    
    # if: only one element
    if self.size == 1:
      self.head = None
      self.tail = None

      self.size -= 1
      return removed
    
    # more than 1
    next = self.head.next
    next.prev = None
    self.head = next
    self.size -= 1

    return removed
  
  # push element to the beginning
  def unshift(self, data):
    new_node = Node2(data)

    # if: empty
    if self.size == 0:
      self.head = new_node
      self.tail = new_node
      self.size += 1
      return
    
    # if: 1 element or more

    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
    self.size += 1
  
  # take an index and return index at that position
  def get(self, index):
    
    # if index out of range
    if index < 0 or index >= self.size:
      return None

    if index == 0:
      return self.head
    
    if index == self.size - 1:
      return self.tail

    # start from start or end of the list, which ever our index is closer to
    distance_to_start = abs(index - 0)
    distance_to_end = abs(index - self.size)

    start_from_tail = distance_to_end < distance_to_start

    current_node = None
    if start_from_tail:
      print('start from tail---')
      current_node = self.tail

      i = self.size - 1
      # don't hit the index =: cause: node.next
      while i > index:
        current_node = current_node.prev
        i -= 1

    else:
      print('start from head---')
      current_node = self.head

      i = 0
      while i < index:
        current_node = current_node.next
        i += 1

    return current_node

  # set node data by index
  def set(self, index, data):
    found_node = self.get(index)
    # if: index does not exists -: None
    if found_node != None:
      found_node.data = data
      return True

    # set was unsuccessful
    return False

  # insert a new node at an index
  def insert(self, index, data):

    # check for out of bound
    if index < 0 or index >= self.size:
      return False

    # index=0 =: just push to start
    if index == 0:
      self.size += 1
      return self.unshift(data)

    # last index =: just push
    if index == self.size - 1:
      self.size += 1
      return self.push(data)

    new_node = Node2(data)

    # get node by index
    target_node = self.get(index)

    if target_node != None:
      prev = target_node.prev

      new_node.next = target_node
      new_node.prev = prev
      prev.next = new_node
      target_node.prev = new_node
      self.size += 1
      return True

    return False

  # remove element by index
  def remove(self, index):

    # check for out of bound
    if index < 0 or index >= self.size:
      return False

    # index=0 =: just shift from start
    if index == 0: 
      self.size -= 1
      return self.shift()

    # last index =: just pop
    if index == self.size - 1:
      self.size -= 1
      return self.pop()

    # get node by index
    target_node = self.get(index)

    if target_node != None:
      prev = target_node.prev
      next = target_node.next

      prev.next = next
      next.prev = prev

      # remove the current target
      target_node = None

      self.size -= 1
      return True

    return False

  # print the list
  def print_list(self):
    current_node = self.head
    list = []

    while current_node:
      list.append(current_node.data)
      current_node = current_node.next
    print(list)
      
node1 = DoublyLinkedList()

node1.push('love')
node1.push('great')
print(node1.pop())
print(node1.pop())
#print(node1.pop())
node1.push('white')
node1.push('red')
print(node1.shift().data)
node1.unshift('sara')
node1.unshift('john')
node1.push(45)
node1.push(46)
node1.push(47)
node1.push(48)

node1.set(1, 'GOOGLE')

node1.insert(2, 'HOT')
node1.remove(3)

print(node1.get(4).data)
#print(node1.head.data, node1.tail.data)

node1.print_list()


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
#=========================================


print('\n------------------------------')