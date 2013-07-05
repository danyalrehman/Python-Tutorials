#author - danyalrehman

def function():

    binarystring = raw_input("Enter a binary number: ")

    list = []
    count = 0

    while (count < len(binarystring)):

        list.append(binarystring[count])
        count += 1

    list.reverse()

    counter = 0
    tracker = 0
    number = 0

    while (counter < len(list)):

        tracker = 2**counter
        number += int(list[counter]) * tracker
        tracker += 1
        counter += 1

    print "This is the normal version of the binary number you entered: " + str(number)


function()
