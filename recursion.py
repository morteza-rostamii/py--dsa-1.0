
import math

print('------------------------------\n')

# calc factorial
# 5 * 4 * 3 * 2 * 1
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

result = factorial(5)
print(result) # 120

#=========================================

# fibonacci
# 0, 1, x =: you get x by adding two positions before x
# x = 0 + 1 = 1
# then: 0, 1, 1, x

def fibonacci(n):
  # base case for zero
  if n == 0:
    return 0
  # base case for 1
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

result2 = fibonacci(8)
print(result2)

#=========================================

# tree traversal

class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.left = None
    self.right = None

# Create a sample tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)  

def pre_order_traversal(root):
  # base case: there is no left or right => return
  if root is None:
    return
  
  print(root.data)
  pre_order_traversal(root.left)
  pre_order_traversal(root.right)

pre_order_traversal(root)

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