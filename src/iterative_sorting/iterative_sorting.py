# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(smallest_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                arr[j], arr[smallest_index] = arr[smallest_index], arr[j] 
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # 1. Loop through your array
    # - Compare each element to its neighbor
    # - If elements in wrong position (relative to each other, swap them)
    # 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    index = 0
    while index < len(arr):
        idx = 0
        while idx < len(arr)-1:
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            idx += 1
        index += 1
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr