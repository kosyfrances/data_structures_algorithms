def list_merge_sort(list1, list2):
    """ Implementing merge sort with the assumption that the two lists coming in
    are sorted already. """
    print "Initial unsorted first list", list1
    print "Initial unsorted second list", list2

    sorted_list = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i = i + 1
            print "i is ", i
            print "sorted list is ", sorted_list
        else:
            sorted_list.append(list2[j])
            j = j + 1
            print "j is ", j
            print "sorted list is ", sorted_list

    while i < len(list1):
        sorted_list.append(list1[i])
        i = i + 1

    while j < len(list2):
        sorted_list.append(list2[j])
        j = j + 1

    print "sorted list is ", sorted_list

list1 = [2, 5, 9]
list2 = [0, 4, 8]
list_merge_sort(list1, list2)
