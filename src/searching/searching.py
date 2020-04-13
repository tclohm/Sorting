# STRETCH: implement Linear Search				
def linear_search(arr, target):
  head = 0
  # TO-DO: add missing code
  if arr[0] == target:
    return 0
  elif arr[0] == len(arr)-1:
    return -1
  else:
    return linear_search(arr[head+1:], target)

   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if low == high:
    return lower
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  elif arr[middle] == target:
    return middle
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle - 1)
  else:
    return binary_search_recursive(arr, target, middle + 1, high)