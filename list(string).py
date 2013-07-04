#author - danyalrehman


def function():

    """ you can make a string into a list using the function list(string) instead of looping through it
    to extract each character
"""

    list1 = list('Danyal Rehman')

    count = 0

    while (count < len(list1)):

        print list1[count]
        count += 1


function()
