
import math

print('------------------------------\n')

"""
how to calculate n! factorial, using a recursion

"""

def calcFactorial(n):
  print(n)
  if n <= 0:
    return 1
  
  return n * calcFactorial(n - 1)

#print(calcFactorial(5))
#print(calcFactorial(1))
#print(calcFactorial(0))

#=========================================

# return an array of all values for n! factorial

def getFactorialValues(n):
  
  # base case 
  if n == 0:
    return []
  else:
    # prepend n to the list 
    # appends and returns a new list
    return [n] + getFactorialValues(n - 1)

#print(getFactorialValues(6))

#=========================================

"""
# search 

28. Find the Index of the First Occurrence in a String
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

def searchSubStr1(haystack, needle):
  """
  :type haystack: str
  :type needle: str
  :rtype: int
  """
  haystack_size = len(haystack)
  needle_size = len(needle)

  # needle is smaller that haystacking
  if haystack_size < needle_size:
    return -1

  # pointer to loop through needle
  p_tar = 0
  p_str = 0

  found_needle = ''

  while p_str < haystack_size:
    print(F"p_str:{p_str}, p_tar:{p_tar}, [p_str]:{haystack[p_str]}, [p_tar]:{needle[p_tar]}")
    print('-**', found_needle)
    # a != b
    if haystack[p_str] != needle[p_tar]:
      print('--wrong')

      # after finding first correct! we failed so: set pointer back
      p_str -= p_tar

      # because of this resetting of the pointer =: O(haystack_size * needle_size)
      # reset the pointer
      p_tar = 0

      # reset
      found_needle = '' 

    else: 
      print('--correct')
      # only move pointer on needle =: if: chars match
      if p_tar < needle_size - 1: 
        p_tar += 1
        
      # ex: haystack[0] == needle[0]
      found_needle += haystack[p_str]

    print(p_str)
    # if: needle is complete return
    if found_needle == needle:
      # to get the starting index of ex: me
      return p_str - (needle_size - 1)

    # move long pointer =: on each wrong 
    p_str += 1

  # can't find the needle
  return -1

#print(searchSubStr1('call me cat', 'me'))
#print(searchSubStr1('call me cat', 'cat'))
#print(searchSubStr1('mississippi', "issip"))

#=========================================

#Knuth-Morris-Pratt (KMP) Algorithm

# def searchStrKMP(haystack, needle):

#   haystack_size = len(haystack)
#   needle_size = len(needle)

#   needle_prefix_size = int(needle_size * .8)
#   needle_prefix = needle[:needle_prefix_size]

#   print(needle_prefix)

# searchStrKMP('goalisgoalyes', 'isgoal')

#=========================================

# Rabin-Karp Algorithm (Optional):

#=========================================

# bubble sort:

def bubbleSort(arr):
  size = len(arr)
  temp = 0

  # - 1 =: cause: we have a i + 1 inside of the loop?!
  for _ in range(0, size - 1):
    # if: you loop 1 time and no swap happens =: arr is sorted
    swapped = False
    for i in range(0, size - 1):
      # move the greater value to the end of array
      if arr[i] > arr[i+1]:
        temp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = temp

        swapped = True

    # if: no swap happens break
    if not swapped:
      break

  return arr

#print(bubbleSort([20, 14, 16, 3, 5]))

#=========================================

# selection sort:

def selectionSort(arr):
  size = len(arr)
  swap = 0

  for i in range(0, size):
    # set current_min to the next index (always initialize with current arr[i], take it as smallest)
    current_min_index = i

    for j in range(i+1, size):

      if arr[j] < arr[current_min_index]:
        # keep the index of smallest value compare to current min
        current_min_index = j
    
    # move arr[i] to where smallest is 
    swap = arr[current_min_index]
    arr[current_min_index] = arr[i]
    arr[i] = swap

    print(arr)

  return arr

#print(selectionSort([24, 2, 5, 11, 1]))
#print(selectionSort([34, 2, 4, 2, 12]))

#=========================================

# insertion sort:

def insertionSort(arr):
  
  size = len(arr)
  swap = None

  for i in range(1, size):
    current_min_index = i

    for j in range(i-1, -1, -1):

      if arr[j] > arr[current_min_index]:
        swap = arr[current_min_index]
        arr[current_min_index] = arr[j]
        arr[j] = swap
        current_min_index = j
        print(i, j)

  return arr

#print(insertionSort([24, 2, 5, 11, 1]))
#print(insertionSort([23, 3, 0, 11, 4]))

#=========================================



#=========================================
#=========================================
#=========================================
#=========================================


print('\n------------------------------')