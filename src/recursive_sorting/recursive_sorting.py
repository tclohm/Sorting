# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( lhs, rhs ):
    elements = len( lhs ) + len( rhs )
    merged_arr = [0] * elements
    # TO-DO
    merged_index, lhs_index, rhs_index = 0, 0, 0
    while lhs_index < len(lhs) and rhs_index < len(rhs):
        if lhs[lhs_index] < rhs[rhs_index]:
            merged_arr[merged_index] = lhs[lhs_index]
            lhs_index += 1
            merged_index += 1
        else:
            merged_arr[merged_index] = rhs[rhs_index]
            rhs_index += 1
            merged_index += 1
    # if one of the sides has more elements to merge after iterating through
    # start from left to right
    while lhs_index < len(lhs):
        merged_arr[merged_index] = lhs[lhs_index]
        lhs_index += 1
        merged_index += 1
    while rhs_index < len(rhs):
        merged_arr[merged_index] = rhs[rhs_index]
        rhs_index += 1
        merged_index += 1

    return merged_arr
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if the list length is 0 or 1, it's sorted
    # if the list has more than two elements, split into two lists and user merge to sort
    # merge the results
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr)//2
        left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])
        print(left, right)
        return merge(left, right)

#print("merge sort:", merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    while start < mid and mid < end:
        if arr[start] > arr[mid]:
            arr[start], arr[mid] = arr[mid], arr[start]
            start += 1
        if arr[mid] > arr[end]
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
middle = (len(arr1)-1) // 2
print(merge_in_place(arr1, 0, middle, len(arr1)-1))
def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if len(arr) < 2:
        return arr
    else:
        return merge_in_place(arr, l, len(arr)//2, r)

# print(merge_sort_in_place(arr1, 0, len(arr1)-1))
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
