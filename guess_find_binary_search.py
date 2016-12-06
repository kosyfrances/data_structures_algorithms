def binary_search(sorted_list, item):
    """
    This binary_search function takes a sorted array and an item.
    If the item is in the array, the function returns its position.
    """

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        print("mid is, ", mid)
        guess = sorted_list[mid]
        print("guess is, ", guess)

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 7, 8, 10]
print(binary_search(my_list, 3))