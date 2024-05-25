
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

# merge sort: 

def merge(left, right, arr):
  left_size = len(left)
  right_size = len(right)

  results = []
  p1 = 0
  p2 = 0
  print(left, right, arr)

  while p1 < left_size and p2 < right_size:

    if left[p1] < right[p2]:
      results.append(left[p1])
      p1 += 1
    elif right[p2] < left[p1]:
      results.append(right[p2])
      p2 += 1 

  print('---', p1, p2)
  # push the remaining
  if p1 < left_size: 
    results.extend(left[p1:])

  if p2 < right_size:
    print('gooo', right[p2:])
    results.extend(right[p2:])
  
  print('__', results)
  return results

def mergeSort(nums):
  
  size = len(nums)
  # base case
  if size <= 1:
    return nums
  
  mid = size // 2
  
  left_half = mergeSort(nums[:mid])
  right_half = mergeSort(nums[mid:])

  #print(left_half, right_half)

  return merge(left_half, right_half, nums)

#print(mergeSort([24, 2, 5, 11, 1, 6]))

#=========================================

# quick sort

# def quickSort(nums):

#   size = len(nums)

#   # base case 
#   if size < 2:
#     return

#   temp = None
#   # pivot is the last index
#   pivot_inx = size - 1

#   i = 0
#   j = 0 

#   while True:
#     print(i, j)

#     if nums[j] < nums[pivot_inx]:
#       # if: j < pivot =: swap i with j
#       swap = nums[i]
#       nums[i] = nums[j]
#       nums[j] = swap

#       # move i only if j < pivot
#       i += 1

#     # move j on each loop
#     j += 1 

#     if j >= size: 
#       break

#     if j == pivot_inx:
#       #i += 1
#       # swap pivot between small and large values
#       swap = nums[i]
#       nums[i] = nums[pivot_inx]
#       nums[j] = swap
#       # last pivot index
#       pivot_inx = i
    

#   left = quickSort(nums[:pivot_inx])
#   # not include the pivot_inx
#   right = quickSort(nums[pivot_inx+1:])

#   print(left, right)
#   return nums

# changing the array we send in directly
def quickSort(nums):
  print('input', nums)
  size = len(nums)

  # base case 
  # array with size less than 2 is sorted 
  if size < 2:
    # we are not returning value we are changing the original array
    return 
  
  # take the middle value as pivot
  pivot_index = size // 2
  pivot = nums[pivot_index]

  # partitioning to smaller that pivot and greater
  smaller = []
  greater = []

  for i in range(0, size):
    # skip pushing the pivot into smaller or greater
    if i == pivot_index:
      continue
    
    # smaller or equal for repeated elements
    if nums[i] <= pivot:
      smaller.append(nums[i])
    # greater
    else:
      greater.append(nums[i])
  
  # recursive
  quickSort(smaller)
  quickSort(greater)

  # rewrite the original array
  nums[:] = smaller + [pivot] + greater
  print(nums)

arr = [24, 2, 5, 11, 1, 6]
quickSort(arr)
print(arr)
#=========================================
#=========================================
#=========================================


print('\n------------------------------')