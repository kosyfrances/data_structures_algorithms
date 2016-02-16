from random import randint

def create_random_array(length):
    return [randint(0, 100000) for i in xrange(length)]

MEMORY_USED = 0
MAX_MEMORY_USED = 0

def merge_sort(a_list):
    global MEMORY_USED, MAX_MEMORY_USED
    """Implementing merge sort from the book - Problem solving with algorithms
    and data structures pdf."""

    print("Splitting ", a_list)

    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        MEMORY_USED += len(left_half)
        right_half = a_list[mid:]
        MEMORY_USED += len(right_half)
        print "Memory used is ", MEMORY_USED

        MAX_MEMORY_USED = max(MAX_MEMORY_USED, MEMORY_USED)
        print "Maximum memory used is ", MAX_MEMORY_USED

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            print "left half from line 13 is ", left_half
            print "right half from line 14 is ", right_half

            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1

            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

        MEMORY_USED -= len(a_list)
        print "Releasing memory, now used:", MEMORY_USED

    print("Merging ", a_list)



#a_list = [54, 26, 93, 17, 77, 31]
# a_list = create_random_array(16)
# merge_sort(a_list)
# print (a_list)
# print "additional memory used:", MAX_MEMORY_USED

# Checking out how much time it takes
from timeit import timeit

setup = 'from __main__ import create_random_array; s_list = create_random_array(128)'
stmt = 'from __main__ import merge_sort; merge_sort(s_list)'
print timeit(stmt, setup, number=10000)

# Length    Time to sort
#     16            0.21
#     32            0.47 = 2 * 0.21 + 0.03
#     64            1.02 = 2 * 0.47 + 0.08
#    128            2.22 = 2 * 1.02 + 0.18

############################

# merge_sort(a_list)
#     -> create 2 lists of length 8                   # allocating 16
#     -> merge_sort(left_half)
#         -> create 2 lists of length 4               # allocating 8
#         -> merge_sort(left_half)
#             -> create 2 lists of length 2           # allocating 4
#             -> merge_sort(left_half)
#                 -> create 2 lists of length 1       # allocating 2
#                 -> merge_sort(left_half)
#                 -> merge_sort(right_half)
#                                                     # freeing 2
#             -> merge_sort(right_half)
#                 -> create 2 lists of length 1       # allocating 2
#                 -> merge_sort(left_half)
#                 -> merge_sort(right_half)
#                                                     # freeing 2
#                                                     # freeing 4
#         -> merge_sort(right_half)
#             -> create 2 lists of length 2           # allocating 4
#             -> merge_sort(left_half)
#                 -> create 2 lists of length 1
#                 -> merge_sort(left_half)
#                 -> merge_sort(right_half)
#             -> merge_sort(right_half)
#                 -> create 2 lists of length 1
#                 -> merge_sort(left_half)
#                 -> merge_sort(right_half)

# Assuming the length of the list is even

# additional memory needed for sorting a list of length 16:
# 16 + 8 + 4 + 2

# additional memory needed for sorting a list of length 32:
# 32 + 16 + 8 + 4 + 2

# additional memory needed for sorting a list of length n:
# n + n/2 + n/4 + n/8 + ... + 2 =  2n - 2


# ('Splitting ', [24304, 12941, 25860, 4181, 81916, 79743, 11704, 84893])
# Memory used is  8
# Maximum memory used is  8
# ('Splitting ', [24304, 12941, 25860, 4181])
# Memory used is  12
# Maximum memory used is  12
# ('Splitting ', [24304, 12941])
# Memory used is  14
# Maximum memory used is  14
# ('Splitting ', [24304])
# ('Merging ', [24304])
# ('Splitting ', [12941])
# ('Merging ', [12941])
# left half from line 13 is  [24304]
# right half from line 14 is  [12941]
# Releasing memory, now used: 12
# ('Merging ', [12941, 24304])
# ('Splitting ', [25860, 4181])
# Memory used is  14
# Maximum memory used is  14
# ('Splitting ', [25860])
# ('Merging ', [25860])
# ('Splitting ', [4181])
# ('Merging ', [4181])
# left half from line 13 is  [25860]
# right half from line 14 is  [4181]
# Releasing memory, now used: 12
# ('Merging ', [4181, 25860])
# left half from line 13 is  [12941, 24304]
# right half from line 14 is  [4181, 25860]
# left half from line 13 is  [12941, 24304]
# right half from line 14 is  [4181, 25860]
# left half from line 13 is  [12941, 24304]
# right half from line 14 is  [4181, 25860]
# Releasing memory, now used: 8
# ('Merging ', [4181, 12941, 24304, 25860])
# ('Splitting ', [81916, 79743, 11704, 84893])
# Memory used is  12
# Maximum memory used is  14
# ('Splitting ', [81916, 79743])
# Memory used is  14
# Maximum memory used is  14
# ('Splitting ', [81916])
# ('Merging ', [81916])
# ('Splitting ', [79743])
# ('Merging ', [79743])
# left half from line 13 is  [81916]
# right half from line 14 is  [79743]
# Releasing memory, now used: 12
# ('Merging ', [79743, 81916])
# ('Splitting ', [11704, 84893])
# Memory used is  14
# Maximum memory used is  14
# ('Splitting ', [11704])
# ('Merging ', [11704])
# ('Splitting ', [84893])
# ('Merging ', [84893])
# left half from line 13 is  [11704]
# right half from line 14 is  [84893]
# Releasing memory, now used: 12
# ('Merging ', [11704, 84893])
# left half from line 13 is  [79743, 81916]
# right half from line 14 is  [11704, 84893]
# left half from line 13 is  [79743, 81916]
# right half from line 14 is  [11704, 84893]
# left half from line 13 is  [79743, 81916]
# right half from line 14 is  [11704, 84893]
# Releasing memory, now used: 8
# ('Merging ', [11704, 79743, 81916, 84893])
# left half from line 13 is  [4181, 12941, 24304, 25860]
# right half from line 14 is  [11704, 79743, 81916, 84893]
# left half from line 13 is  [4181, 12941, 24304, 25860]
# right half from line 14 is  [11704, 79743, 81916, 84893]
# left half from line 13 is  [4181, 12941, 24304, 25860]
# right half from line 14 is  [11704, 79743, 81916, 84893]
# left half from line 13 is  [4181, 12941, 24304, 25860]
# right half from line 14 is  [11704, 79743, 81916, 84893]
# left half from line 13 is  [4181, 12941, 24304, 25860]
# right half from line 14 is  [11704, 79743, 81916, 84893]
# Releasing memory, now used: 0
# ('Merging ', [4181, 11704, 12941, 24304, 25860, 79743, 81916, 84893])
# [4181, 11704, 12941, 24304, 25860, 79743, 81916, 84893]
# additional memory used: 14
