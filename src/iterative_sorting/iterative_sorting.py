# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # 1. find min element
        # swap it with index 0
    # iterative step
        # sublist, extract minimum element
        # swap it with the element at index 1, 2, 3, ..., n
    # keep the left portion of the list sorted
        # at the nth step, first elements in list are sorted
        # all other elements are bigger than first n elements 
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
    # step through our list, this is our big container
        # step through the list again, for iteration through or big container
            # switch if the arr[n] is greater than arr[n + 1]
            # move forward
        # once our iterations are done, move to the next row to check if everything is
    # index = 0
    # while index < len(arr):
    #     idx = 0
    #     swap = False
    #     while idx < len(arr)-1:
    #         if arr[idx] > arr[idx + 1]:
    #             arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    #             swap = True
    #             print("swap")
    #         idx += 1
    #         print(arr)
    #     index += 1

    #     if swap == False:
    #         print("break!")
    #         return arr
    rotation = 0
    # change to while loop and flag if no swap occurs
    for row in range(0, len(arr)-1):
        print("row", row)
        print(f"arr:{len(arr)-1} - 1 - row:{row} = ", len(arr) - 1 - row)
        for column in range(0, len(arr) - 1 - row):
            if arr[column] > arr[column + 1]:
                arr[column], arr[column +1] = arr[column + 1], arr[column]
            rotation += 1
            print("rotate:", rotation)
    return arr


#print(bubble_sort([1, 2, 3, 5, 4, 9, 11, 10, 16, 15, 14, 32, 44, 0]))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    """
        iterate through the input, count the number of times each item occurs
        using the counts, compute an item's index in the final list
        ex: [1, 1, 3, 2, 1],
            [0, 0, 0, 0, 0]
         pos[0, 1, 2, 3, 4]
            [0, 3, 1, 1, 0]
    """
    return arr

count_sort([5, 1, 2, 4, 5, 3, 3, 3], 7)