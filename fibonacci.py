__author__ = 'danyalrehman'

def fibonacci(n):
    """ the aim of this function is to ive the series
    of fibonacci numbers all the way until the inputted
    number, n.
    """
    
    sublist = []
    fibo_list = []
    count = 1
    count2 = 0

    while count <= n:
        sublist.append(count)
        count += 1
    print sublist
    for eachnumber in sublist:
        fibo_list.append((sublist[eachnumber - 1] + sublist[count2]))
        count2 += 1
    return fibo_list

print fibonacci(9)