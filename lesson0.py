
name = "Morteza Rostami"

print('------------------------------\n')

"""
write a function that accepts a string input and returns a reversed copy.

"""

# simple way is to loop the string backward
# O(n)
def reverseStr(str_input:str):
  size:int = len(str_input) 
  reversed = ''
  
  # start are 3, not include -1, step: -1 subs 1 in each loop
  for i in range(size - 1, -1, -1):
    reversed += str_input[i]

  return reversed

#reversed_str:str = reverseStr('cat') 
reversed_str:str = reverseStr('love') 

#print(reversed_str)

#=============================================

"""
# big O

Constant Time (O(1))
Logarithmic Time (O(log n))
Linear Time (O(n))

# 2 independent inputs to the function
O(n + m)

Linearithmic Time (O(n log n))
Quadratic Time (O(n^2))
Polynomial Time (O(n^x) where x > 2)
Exponential Time (O(2^n))
Factorial Time (O(n!))



""" 

#=============================================

"""
# write a function that calcs the sum of all numbers from 1 up to and (including) some number "n"

# O(1)
formula

sum of n natural numbers = n * (n+1) / 2
"""
# O(1)
def sumNumbers1(n):
  return n * (n+1) / 2

#print(sumNumbers1(4)) # 10.0

# O(n)
def sumNumbers2(n):
  res = 0
  # add 1 to n =: cause range() does not include up to n
  for i in range(1, n + 1):
    res += i
  return res

#print(sumNumbers2(4))

#=============================================

"""
# looping through a matrix

"""

matrix = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
]

# 2*4 simplifies to = n*n =: O(n^2) 
def loopThroughMatrix(matrix):  
  for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
      print(F"i:{i} - j:{j} = [{matrix[i][j]}]")

#loopThroughMatrix(matrix)

#=============================================

# dic
my_dict = {
  "name": 'ali',
  "age": 23,
}

#print(my_dict['name'])

#=============================================

"""
# understand the big picture of your problem
  # in general x`what are you trying to solve?
  # restate the problem in your own words

# what are inputs and expected outputs?
  # how can you get the output from the given input?! 

# label each piece of data given by the problem.
# break the big problem into small problems.

# define input and output for each small problem.
  # make a list of all the things you need to do to solve the problem. 
  # ask what are 2 possible ways to do task x
    # ex: drawing a paddle on screen or moving the paddle up and down.

# explore possibilities: 
  # empty input
  # invalid input and so on

# write pseudo code

# write code

"""

#=============================================

"""
# write a function that returns count of each character in a string.

"babadoo" =: 0: 2
"""

# O(n)
def countCharOccurrence(input:str):

  count = {
    # b: 2
  }

  for i in range(0, len(input)):
    # if: there is no: "b": 0 , key:value inside dict
    if not(input[i] in count):
      count[input[i]] = 0
      count[input[i]] += 1
    else:
      count[input[i]] += 1

  return count

#char_count = countCharOccurrence('babadoo')
#print(char_count)
#{'b': 2, 'a': 2, 'd': 1, 'o': 2}

#=============================================

# patterns:

"""
# Frequency counter
# Multiple Pointers
# Sliding Window
# Divide and counter
# dynamic Programming
# Greedy algorithms
# Backtracking
# ...

"""

#=============================================

"""
write a function called same, which accepts two arrays. 
if: every value in the array has it's corresponding values squared in the second array:
  return: true

# the frequency of values must be the same. order does not matter 

in: [1, 2, 3] out: [4, 1, 9] // true
in: [1,2 ,3] out: [1, 9] // false
in: [1, 2, 1] out: [4, 4, 1] // false (frequency is not the same)

"""

# two array are passed in that might have really different sizes
# we have two loops that are completely independent of each other. meaning loop through different arrays
# so: O(n + m)
def same(arr1, arr2):
  # arrays must be the same size
  if len(arr1) != len(arr2):
    return False

  # frequency counter
  count_squares = {}
  for i in range(0, len(arr2)):
    if not(arr2[i] in count_squares):
      count_squares[arr2[i]] = 0
      count_squares[arr2[i]] += 1
    else:
      count_squares[arr2[i]] += 1

  # loop arr1 and square each
  for i in range(0, len(arr1)):
    square = arr1[i] ** 2
    # if: not squared at all
    if (not(square in count_squares)):
      return False

    # if: is squared more than once
    if (count_squares[square] > 1):
      return False

  return True

#is_squared_once = same([1,2,3], [4,1,9])
#is_squared_once = same([1,2,3], [1,9])
#is_squared_once = same([1,2,1], [4,4,1])

#print(is_squared_once)

#=============================================

# anagrams:

"""
Given two strings, write a function to determine if the second string is an anagram of the first.
an anagram is a word, phrase of name formed by rearranging the letters of another, such as cinema, formed from iceman.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. There shouldn't be any extra or missing letters in an anagram compared to the original word.

('', '') // true
('aaz', 'zza) // false
('qwerty', 'qeywrt') // true

"""

# O(n+m)
def isAnagram(a:str, b:str) -> bool:

  # different length means: not anagram
  if (len(a) != len(b)):
    return False
  
  # count number of occurrence of each char 
  frequency_counter = {}
  for i in range(0, len(b)):
    if not(b[i] in frequency_counter):
      frequency_counter[b[i]] = 0
      frequency_counter[b[i]] += 1
    else:
      frequency_counter[b[i]] += 1

  # loop a
  for i in range(0, len(a)):
    # if: letter does not exists: it is not an anagram
    if not(a[i] in frequency_counter):
      return False

    # if: we have an occurrence: stay True
    if frequency_counter[a[i]] > 0:
      # remove one occurrence
      frequency_counter[a[i]] -= 1
    else:
      # no more occurrence
      return False

  return True

#print(isAnagram('cat', 'tac'))
#print(isAnagram('caat', 'taac'))
#print(isAnagram('', ''))
#print(isAnagram('qwerty', 'qeywrt'))
#print(isAnagram('aaz', 'zza'))

#=============================================

# Multiple Pointers
"""
create pointers or values that correspond to an index or position and move towards the beginning, end or middle.

 a                 b
[1, 34, 4, 6, 32, 65]

# ex

# write a function called sumZero which accepts a sorted array of integers. 
the function should find the first pair where the sum is 0.
return an array that includes both values that sum to zero or undefined if a pair does not exist.

sorted:
[-6, -4, 1, 4, 6, 32, 40]

0 + 0 = 0
-5 + 5 = 0
opposite + opposite = 0 
"""

def sumZero(arr):
  size = len(arr)
  if size <= 1: 
    return None

  # first index
  pointer_a = 0
  # last index
  pointer_b = size - 1
  sum = None

  while True:

    sum = arr[pointer_a] + arr[pointer_b]

    if (sum == 0):
      return [arr[pointer_a], arr[pointer_b]]

    # if: a != b and a and be are at last index
    if pointer_a == size - 1:
      break

    pointer_b -= 1

    # looking for: -5, 5 but b=4
    if abs(arr[pointer_b] < arr[pointer_b]):
      pointer_a += 1
      pointer_b = size - 1

    if (pointer_a == pointer_b):
      pointer_a += 1
      pointer_b = size - 1

  return None

#res = sumZero([-6, -4, 1, 4, 6, 32, 40])
#res = sumZero([-3, -2, -1, 0, 1, 2, 3])
#res = sumZero([-2, 0, 1, 3])
#res = sumZero([1, 2, 3])
#res = sumZero([5])
#res = sumZero([-5, 5])

#print(res)

# slightly different version of above function
def sumZero2(arr):
  size = len(arr)
  if size <= 1:
    return None
  
  left = 0
  right = size - 1
  sum = None

  while True:
    sum = arr[left] + arr[right]
    if sum == 0:
      return [arr[left], arr[right]]

    # if: left = right and not sum = 0 =: break
    if left == right:
      break
    
    # [-4, ... , 10]
    # if: sum > 0 =: means: far left is smaller that far right and there is no opposite for far right: so right--
    elif sum > 0:
      right -= 1
    # sum: is negative =: means: there is no opposite for far left
    # so move left++
    else:
      left += 1

  return None     

#res = sumZero([-6, -4, 1, 4, 6, 32, 40])
#res = sumZero([-3, -2, -1, 0, 1, 2, 3])
#res = sumZero([-2, 0, 1, 3])

#print(res)

# to find combinations of 2 pairs of elements.

# nested loop

# O(n^k) or O(n^2)
def printAllCombinations1(arr):
  for i in range(0, len(arr)):
    # start from 1
    for j in range(i+1, len(arr)):
      print(F"({arr[i]}, {arr[j]})\n")

#printAllCombinations1([1, 3, 5, 7])

#=============================================

"""
implement a function called countUniqueValues.
which accepts a sorted array. and counts the unique values in the array.
there can be negative numbers in the array, but it will always be sorted.

"""

def countUniqueValues(arr):
  size = len(arr)
  if size <= 1:
    return 0
  
  # two pointer method
  p1 = 0
  p2 = p1 + 1
  unique_count = 0

  while True:
    print(p1, p2)
    if arr[p1] != arr[p2]:
      unique_count += 1
      p1 = p2

      # if: p1 != p2 and p2 is the last index
      if p2 == size - 1:
        unique_count += 1

      if p2 < size - 1:
        p2 += 1
    else:
      p2 += 1

    if p1 == size - 1 and p2 == size - 1:
      break
  
  return unique_count

#res = countUniqueValues([1, 1, 1, 1, 1, 2])
#res = countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])
#res = countUniqueValues([])
#res = countUniqueValues([-2, -1, -1, 0, 1])
#print(res)

"""
 a  b
[1, 2, 3, 4, 4, 4]
"""

def countUniqueValues2(arr):
  size = len(arr)
  if size <= 0:
    return 0
  if size == 1:
    return 1

  left = 0
  right = left + 1

  while True:

    if arr[left] != arr[right]:
      # move left +1
      left += 1
      # accumulate unique elements in the beginning of arr
      arr[left] = arr[right]
      # move right
      right += 1
    else:
      # it is the same value: move right
      right += 1

    if right == size:
      break
  
  uniques = arr[:left+1]

  return len(uniques)

#print(countUniqueValues2([1, 2, 3, 4, 4, 4]))
#print(countUniqueValues2([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))
#print(countUniqueValues2([]))
#print(countUniqueValues2([-2, -1, -1, 0, 1]))



#=============================================

#=============================================

print('\n------------------------------')
