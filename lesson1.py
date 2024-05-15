import math

print('------------------------------\n')

"""
# sliding window:

write a function called maxSubArraySum which accepts an array of integers and a number called n.
the function should calculate the maximum sum of n consecutive elements in the array.

"""

def maxSubArraySum(arr, num):
  size = len(arr)

  # array length is smaller that number of consecutive elements.
  if size < num:
    return None
  
  max_sum = -math.inf
  temp_sum = 0

  # initial sum: first n consecutive elements
  for i in range(0, num):
    temp_sum += arr[i]

  # first maximum sum
  max_sum = temp_sum

  p1 = 0
  p2 = num - 1

  while True:
    p1 += 1
    p2 += 1

    # if: only 3 [1,2,3] here p2 = 3 = size =: so: breaks.
    if p2 == size:
      break
    
    temp_sum = temp_sum - arr[p1 - 1] + arr[p2]
    
    if temp_sum > max_sum:
      max_sum = temp_sum
        
  return max_sum

#print(maxSubArraySum([1, 2, 3], 3))
#print(maxSubArraySum([1, 2, 3, 4, 5, 6], 3))
#print(maxSubArraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))

"""
divide and conquer:
==

# Given a sorted arr of integers, 
write a function called search, 
that accepts a value and returns the index where the value passed to the function is located.
if the value is not found, return -1

"""

# Binary search
# O(log n)
def search(arr, target):
  
  size = len(arr)

  left = 0
  right = size - 1
  mid = None

  while left <= right: 
    # calculate the mid
    mid = math.floor((left + right) / 2.0)
    print(mid)
    if arr[mid] == target:
      return mid
    # if: mid is less that target =: target has to be bigger
    elif arr[mid] < target:
      left = mid + 1
    elif arr[mid] > target:
      right = mid - 1
    
  # could not find the target
  return None

#print(search([1, 2, 4, 6, 88, 555], 555))
# print(search([1, 2, 3, 4, 5, 6], 4))
#print(search([1, 2, 3, 4, 5, 6], 6))
#print(search([1, 2, 3, 4, 5, 6], 11))

#=========================================

# recursion

elements = [1, 2, 3, 4, 5]

# use recursion to loop an array
def loopList(arr, i=0):
  size = len(arr)

  # base case
  if i >= size:
    return
  
  print(arr[i])
  i += 1

  # recursive call
  loopList(arr, i)
  

#loopList(elements)

#=========================================

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

"""

def isPalindrome(x:int):

  # convert int to str
  x_str = str(x)
  size = len(x_str)
  reversed_str = ''

  # reverse the string
  for i in range(size - 1, -1, -1):
    reversed_str += x_str[i]

  if reversed_str == x_str:
    return True
  
  return False

#print(isPalindrome(121))

#=========================================

"""

9 9 8 1
5 6 2 6
8 2 6 4
8 2 2 2

9 9 8
5 6 2
8 2 6

9 8 1 
6 2 6
2 6 4

5 6 2
8 2 6
8 2 2

6 2 6
2 6 4
2 2 2

"""
matrix = [
  [9, 9, 8, 1],
  [5, 6, 2, 6],
  [8, 2, 6, 4],
  [8, 2, 2, 2]
]

def  get_sub_matrices(matrix):

  sub_matrices = []
  n = len(matrix)

  for row in range(0, n - 2):
    for col in range(0, n - 2):
      sub_matrix = []

      for i in range(3):
        sub_matrix.append(matrix[row + i][col:col + 3])
      
      # append the sub matrix
      sub_matrices.append(sub_matrix)

  return sub_matrices

def findMaxInEachMatrix(sub_matrices):

  sub_matrices_size = len(sub_matrices)
  #max_matrix_size = math.floor(sub_matrices_size / 2.0)
  max_matrix = []

  for i in range(0, sub_matrices_size):
    max_val = -math.inf
    sub_matrix = sub_matrices[i]

    for row in sub_matrix:
      
      for col in range(0, len(row)):
        if row[col] > max_val:
          max_val = row[col]
    
    # create the max_matrix
    max_matrix.append(max_val)

    print('-----', i, max_val)
  
  return max_matrix

# covert 1d array to 2d array
def to2dArr(arr, max_row):
  matrix = []
  row = []
  counter = 1

  for i in range(0, len(arr)):
    row.append(arr[i])
    print(i, counter, counter % 2)
    if counter % (max_row) == 0:
      
      matrix.append(row)
      row = []
    
    counter += 1

  return matrix

#sub_matrices = get_sub_matrices(matrix)
#max_matrix = findMaxInEachMatrix(sub_matrices)
#print(to2dArr(max_matrix, len(matrix) - 2))

matrix2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

#sub_matrices2 = get_sub_matrices(matrix2)
#max_matrix = findMaxInEachMatrix(sub_matrices2)
#print(to2dArr(max_matrix, len(matrix2) - 2))

#=========================================

# reman Integers

"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

"""

def romanToInt(s: str) -> int:
  size = len(s)
  symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
  }
  
  if size == 0:
    return 0
  
  if size <= 1:
    return symbols[s[0]]

  # roman =to: int
  converted_int: int = 0
  
  # two pointers 
  p1 = 0
  p2 = p1 + 1

  while True:
    print(p1, p2)
    temp_result: int = 0
    # check for subtraction
    if s[p1] == 'I' and (s[p2] == 'V' or s[p2] == 'X'):
      temp_result = symbols[s[p2]] - symbols[s[p1]]
      
    elif s[p1] == 'X' and (s[p2] == 'L' or s[p2] == 'C'):
      temp_result = symbols[s[p2]] - symbols[s[p1]]
  
    elif s[p1] == 'C' and (s[p2] == 'D' or s[p2] == 'M'):
      temp_result = symbols[s[p2]] - symbols[s[p1]]

    # add result of sub
    if temp_result > 0:
      print('temp_sub: ', temp_result, s[p1], s[p2], converted_int)
      converted_int += temp_result

      # if: sub =: move pointers differently
      p1 = p2 + 1
      p2 = p1 + 1

      # break condition
      if p2 >= size:
        # sub move differently =: don't lost the last index
        if p1 < size:
          converted_int += symbols[s[p1]]
        break
      continue

    # no sub so: add p1 & p2
    converted_int += symbols[s[p1]]  
    #converted_int += symbols[s[p2]]  

    # if: p1 and p2 =: not subtraction =: add p2 
    if p2 == size -1:
      converted_int += symbols[s[p2]]
    
    # move pointer
    # move p1 and p2 to ex: after IV=4 or adding: I + I
    print(s[p1], s[p2])
    print('int:: ', converted_int, p1, p2)
    p1 += 1
    p2 += 1
    # if: p2 is out of bound
    if p2 >= size: 
      break

  return converted_int

#print(romanToInt('IIII'))
#print(romanToInt('MCMXCIV'))
#print(romanToInt('LVIII'))
#print(romanToInt('MDCXCV'))
#print(romanToInt('X'))

#=========================================

# O(n)
def longestCommonPrefix(strs):

  # if: list is empty
  if not len(strs):
    return ''

  min_size_element = len(strs[0])
  max_size_element = len(strs[0])
  print('--')
  # if any of strings are empty there is no common prefix
  for i in range(0, len(strs)):

    # get the size of smallest string in the strsay.
    if len(strs[i]) < min_size_element:
      min_size_element = len(strs[i])

    if len(strs[i]) > max_size_element:
      max_size_element = len(strs[i])

    # if: one string empty return 
    if not len(strs[i]):
      return ''

  # longest common prefix
  # take the whole strs[0] str as the common prefix
  common_prefix = list(strs.pop(0))
  common_prefix_size = len(common_prefix)

  # add zeros to the end of common prefix to make it as long as the longest string in the array
  if common_prefix_size < max_size_element:
    diff = max_size_element - common_prefix_size
    for i in range(0, diff):
      common_prefix.append(0)

  # if: smallest = 1 =: set every index from 1 to end to 0
  for i in range(min_size_element, common_prefix_size):
    common_prefix[i] = 0

  # loop over common_prefix
  pointer1 = 0

  # flat the arr of string into string
  arr_str = ','.join(strs)
  size = len(arr_str)

  # if: the first char that it's not common set this to true
  smallest_uncommon_inx = float('inf')
  is_uncommon = False
  
  for i in range(0, size):

    if arr_str[i] == ',':
      # to go from the beginning of common_prefix
      pointer1 = 0
      continue
    
    # found the first one that it's not in common
    
    if arr_str[i] != common_prefix[pointer1]:
      common_prefix[pointer1] = 0
      is_uncommon = True
      # first index in common_prefix that was not common with on of the other strings
      if pointer1 < smallest_uncommon_inx:
        smallest_uncommon_inx = pointer1

    pointer1 += 1

  # from first uncommon index forward: set everything to zero
  # 'cat' and 'cot' =: prefix is: c
  
  # the case: all strings chars are in common
  if is_uncommon:
    for i in range(smallest_uncommon_inx, common_prefix_size):
      common_prefix[i] = 0

  print(common_prefix)
  # get every none zero elements
  non_zeros_are_common = [el for el in common_prefix if el != 0]
  if not len(non_zeros_are_common):
    return ''
    
  longest_common_prefix = ''.join(non_zeros_are_common)
  return longest_common_prefix

#letters1 = ["flower","flow","flight"]
#print(longestCommonPrefix(letters1))

#letters2 = ["dog","racecar","car"]
#print(longestCommonPrefix(letters2))

#print(longestCommonPrefix(['', 'dog']))
#print(longestCommonPrefix(['cat', 'call', '']))
#print(longestCommonPrefix(['cat', 'c']))
#print(longestCommonPrefix(["cir","car"]))
#print(longestCommonPrefix(["c"]))
#print(longestCommonPrefix(["a","cc"]))
#print(longestCommonPrefix(["a","ac"]))
#print(longestCommonPrefix(["baab","bacb","b","cbc"]))

#=========================================

def longestCommonPrefix(strs):

  # if: list is empty
  if not len(strs):
    return ''

  shortest_str = min(strs, key=len)

  for i, char in enumerate(shortest_str):
    for other_str in strs: 
      if other_str[i] != char:
        # found the first uncommon index
        return shortest_str[:i]

  # if: all chars of shortest str are common
  return shortest_str


#letters1 = ["flower","flow","flight"]
#print(longestCommonPrefix(letters1))

#letters2 = ["dog","racecar","car"]
#print(longestCommonPrefix(letters2))

#print(longestCommonPrefix(['', 'dog']))
#print(longestCommonPrefix(['cat', 'call', '']))
#print(longestCommonPrefix(['cat', 'c']))
#print(longestCommonPrefix(["cir","car"]))
#print(longestCommonPrefix(["c"]))
#print(longestCommonPrefix(["a","cc"]))
#print(longestCommonPrefix(["a","ac"]))
#print(longestCommonPrefix(["baab","bacb","b","cbc"]))
#=========================================

# valid parenthesis

"""
so considering stack is last in first out, we have to close the last open symbol !! ex: '(' with ')' !! before we close the symbols we opened before that ! otherwise string is invalid! 

here
"([)]"
we try to close: "(" =: "([)" before we close the last one we opened: "["

"[" is on top of stack and we compare it ")"

You've absolutely nailed the concept! You're right on all points.

Key Points:

Match with the Last Opened: In a valid string, each opening bracket needs to be closed by its corresponding closing bracket, following a last-in-first-out (LIFO) principle. The stack helps us ensure this by keeping track of the opening brackets we encounter.
Stack and Mismatch Detection: As you process the string, you push opening brackets onto the stack and check the top element when you encounter a closing bracket. If the top element doesn't match the type of closing bracket, it means the closing bracket is trying to close something that wasn't opened yet, making the string invalid.
"([)]" Example Breakdown:

Encounter (: Push it onto the stack (stack: ().
Encounter [: Push it onto the stack (stack: [, ().
Encounter ): Check the top element (which is [). Since ) doesn't match [, it's trying to close something that wasn't opened yet, making the string invalid at this point.
"""

# stack
class Stack:
  def __init__(self):
    self.items = []

  # Check if the stack is empty
  def isEmpty(self):
    return self.items == []

  # Push an element onto the stack
  def push(self, item):
    self.items.append(item)

  # Pop (remove) the top element from the stack
  def pop(self):
    if self.isEmpty():
      raise Exception("Stack is empty")
    return self.items.pop()

def isValid(s):
  """
  :type s: str
  :rtype: bool
  """
  
  valid_symbols = {
    "(": '(',
    ")": ')',
    "{": '{',
    "}": '}',
    "[": '[',
    "]": ']',
  }

  closing_match = {
    '(': ')',
    '{': '}',
    '[': ']',
  }
  
  str_arr = list(s)
  str_arr_size = len(str_arr)
  
  # if: string empty
  if not str_arr_size:
    return False
  
  # if: only one symbol
  if str_arr_size <= 1:
    return False
  
  # if: invalid symbol
  for i in range(0, str_arr_size):
    if not str_arr[i] in valid_symbols:
      return False
  
  # stack for pushing opening symbols
  stack = Stack()
  
  for item in str_arr:
    
    # if item is opening push to stack
    if item in closing_match:
      stack.push(item)

    else:
      # it's a closing match

      # if: we have an item and stack empty: means: it's a closing without any opening
      if stack.isEmpty():
        return False

      # pop out the last in an compare it with the closing, 
      # if: equal =: move to next 
      # else: invalid string
      last_opening = stack.pop()
      if closing_match[last_opening] != item:
        return False

  # if: we are out of loop and still have opening symbol inside stack
  # means: never closed them and it's invalid 
  if not stack.isEmpty():
    return False

  # if: can't find a false situation =: then: True 
  return True

#print(isValid('()[]]{}'))
#print(isValid('()'))
#print(isValid('()[]{}'))
#print(isValid('(]'))
#print(isValid('{[]}'))

#=========================================
#=========================================

print('\n------------------------------')