#author - danyalrehman


def function():

    """ Goes through some of the inbuilt functions in Python
    """

    """ This one goes through the append function
    """

    list = ["Danyal", "Daanish", "Deena"]

    list.append("Farazeh")
    list.append("Ahmed")
    list.append("Danyal")

    count = 0

    while (count < len(list)):

        print list[count]
        count += 1

    """ This method is the count method
    """
    print "\n"
    print list.count("Danyal")

    """ This method is the extend function
    """

    list2 = ["Dog", "Cat"]

    list.extend(list2)
    count2 = 0

    while (count2 < len(list)):
        print list[count2]
        count2 += 1

    """ Using the index function
    """

    print list.index("Deena")

    """ Goes through the insert method
    """

    list.insert(5, "Weird")

    count3 = 0

    while (count3 < len(list)):

        print list[count3]
        count3 += 1

    """ Goes through the pop method. Removes the index provided.
    """

    print "\n"

    x = list.pop(2)
    print x

    """ Goes through the remove method
    """

    list.remove("Danyal")

    count4 = 0

    while (count4 < len(list)):

        print list[count4]
        count4 += 1

    print "\n"
    """ Using the reverse method
    """

    list.reverse()

    count5 = 0

    while(count5 < len(list)):

        print list[count5]
        count5 += 1



function()
