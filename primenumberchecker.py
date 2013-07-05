#author - danyalrehman

def function():

    x = int(raw_input("Please enter a number: "))

    count = 1
    list = []

    while (count <= x):

        if (x % count == 0):

            list.append(count)
        count += 1


    if (len(list) == 2):
        print str(x) + " is a prime number"
    else:
        print str(x) + " is not a prime number"




function()
