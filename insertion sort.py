__author__ = 'danyalrehman'

def insertion_sort(unsorted_list):
    """ the aim of this function is to sort a list using the
    selection sort method. This method looks at every element
    in the list and everything after that element and then takes
    the number and puts it in it's appropriate position.
    """
    sorted_list = []

    # the aim of the for loop itself is to look at the smallest
    # number in the unsorted list, append it to the sorted list
    # it then removes the smallest number that is in the unsorted list
    # (the number that was just appended)
    
    for eachnumber in range(len(unsorted_list)):
        smallest_number = min(unsorted_list)
        sorted_list.append(smallest_number)
        unsorted_list.remove(smallest_number)
    return sorted_list

print insertion_sort([1,2,1,4,3,6,4,6,8,9])

def dictionary():
    """ the aim of the function is to take in all the letters of the
    alphabet and assign them to numerical values. This then creates a
    dictionary that has all the keys as the alphabet adn the values as
    the numbers. This dictionary can then be called whenever it
    is required.
    """

    keystring = "abcdefghijklmnopqrstuvwxyz"
    dictionary = {}
    count = 1

    for eachletter in keystring:
        dictionary[eachletter] = count
        count += 1
    return dictionary

print dictionary()