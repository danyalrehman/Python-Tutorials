#author - danyalrehman

def function():

    x = int(raw_input("Enter a number: "))

    count = 1
    tracker = 1
    newtracker = 0
    list = []
    main_list = []

    while (count <= x):

        while (tracker <= count):

            if (count % tracker) == 0:
                list.append(tracker)
                tracker += 1
            else:
                tracker += 1

        if (len(list) == 2):
            main_list.append(count)

        tracker = 1
        count += 1


        list = []

    final_var = 0

    while final_var < len(main_list):

        print str(main_list[final_var])
        final_var += 1

    print "All the numbers above are prime"

function()
