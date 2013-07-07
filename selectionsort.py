__author__ = 'danyalrehman'

def selection_sort(list_1):

    """ selection sorts the list
    """

    list = []
    for i in range(len(list_1)):
        list.append(min(list_1))
        list_1.remove(min(list_1))
    return list

print selection_sort([1,3,5,4,7])

def insertion_sort(list1):
    """ insertion sort
    """
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] < list1[j]:
                z = list1[j]
                list1[j] = list1[i]
                list1[i] = z
        list1[i] = list1[i]
    return list1

print insertion_sort([1,3,2,4,6,7])

def add_neighbours(list):

    i = 0
    list1 = []
    list2 = []
    for i in list:
        list2.append(i)
    while i < len(list2) - 1:
        if list2[i + 1] == type(int) and list2[i - 1] != type(int) :
            list1.append(list2[i] + list2[i + 1])
            i += 1
        elif list2[i + 1] == type(int) and list2[i - 1] == type(int):
            list1.append(list2[i -1] + list2[i] + list2[i + 1])
            i += 1
        elif list2[i - 1] == type(int) and list2[i + 1] != type(int):
            list1.append(list2[i] + list2[i - 1])
            i = len(list2)
    return list1

print add_neighbours([1,3,5,7])

def merge_sort_r(list2, first, last):
    if first < last:
        sred = (first + last)/2
        merge_sort_r(list2, first, sred)
        merge_sort_r(list2, sred + 1, last)
        merge(list2, first, last, sred)

print merge_sort_r([1,2,3,2,3,5,4,6,5,7,6,8,7,8], 0, -1)

