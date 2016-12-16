# A recursive function to count the number of items in a list.


def count_num_list(arr):
    if not arr:
        return 0

    arr.pop()

    return 1 + count_num_list(arr)


print(count_num_list([2, 5, 7, 9, 4]))
