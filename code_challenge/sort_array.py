# Input: [5,2,3,1]
# Output: [1,2,3,5]
# Implements merge sort

def test_split_even():
    input = [5,2,3,1]

    actual = split(input)

    assert(actual == ([5, 2], [3,1]))

def test_split_odd():
    input = [5,2,3,1,4]

    actual = split(input)

    assert(actual == ([5, 2], [3,1, 4]))

def test_merge_even():
    input = [5,2,3,1]
    output = [1,2,3,5]

    actual = merge_sort(input)

    assert(actual == output)

def test_merge_odd():
    input = [5,2,3,6,1]
    output = [1,2,3,5,6]

    actual = merge_sort(input)

    assert(actual == output)

def test_merge_empty():
    input = []
    output = []

    actual = merge_sort(input)

    assert(actual == output)

def test_merge_one():
    input = [2]
    output = [2]

    actual = merge_sort(input)

    assert(actual == output)

def split(arr):
    midpoint = len(arr)//2  #2
    first = arr[:midpoint]  # arr[:2] ==> [5,2]
    second = arr[midpoint:] # arr[2:] ==> [3,1,4]
    return first, second    # [5,2], [3,1,4]

def merge_sort(arr):
    if len(arr) <= 1: # [] or [1]
        return arr
    first, second = split(arr) # [5,2], [3,1,4]
    sorted_first = merge_sort(first) # sorted_first = [5, 2]
    sorted_second = merge_sort(second) # sorted_second = [3, 1, 4]

    sorted_list = [] # sorted_list = []
    i = 0
    j = 0

    while i < len(sorted_first) and j < len(sorted_second):
        if sorted_first[i] < sorted_second[j]:
            sorted_list.append(sorted_first[i])
            i += 1
        else:
            sorted_list.append(sorted_second[j])
            j += 1

    while i < len(sorted_first):
        sorted_list.append(sorted_first[i])
        i += 1

    while j < len(sorted_second):
        sorted_list.append(sorted_second[j])
        j += 1
    return sorted_list # [2, 5]



if __name__ == "__main__":
    test_split_even()
    test_split_odd()
    print("Test merge even")
    test_merge_even()
    print("Test merge odd")
    test_merge_odd()
    print("Test merge empty")
    test_merge_empty()
    print("Test merge one")
    test_merge_one()
