# STRETCH: implement Linear Search				
def linear_search(arr, target):
  # TO-DO: add missing code
  if len(arr) == 0:
    return -1
  for index in range(0, len(arr)):
    if arr[index] == target:
      return index
  return -1
    

print(linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], -6))

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
    middle = (high + low) // 2
    print("high:", high, "low:", low, "middle:", middle)
    if arr[middle] < target:
      low = middle + 1
    if arr[middle] > target:
      high = middle - 1
    if arr[middle] == target:
      return middle
  return -1

print(binary_search(['apples', 'bananas', 'bread', 'chicken', 'coffee', 'dill', 'eggplant', 'meat', 'orange', 'yogurt', 'zeta'], 'zeta'))
# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if low == high:
    return low
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