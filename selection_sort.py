def find_smallest(arr):
    """A function to find the index of the smallest element in an array."""
    smallest_num = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_index = i
    return smallest_index

# Now we can use the find_smallest function to write a selection sort function
def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print selection_sort([5, 3, 6, 2, 10])