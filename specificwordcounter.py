__author__ = 'danyalrehman'

def specificwordcounter(filename, word):
    """ the aim of this function is to read an entire file,
    and then count the number of times a word that was
    entered appears in the entire file.
    """

    reader = open(filename, "r")
    sublist = []
    newer_sublist = []
    count = 0

    for line in reader:
        line = line.strip("\n")
        line = line.split(" ")
        sublist.append(line)
    for eachsublist in sublist:
        if word in eachsublist:
            count += 1
        else:
            count += 0
    return count




print specificwordcounter("something.txt", "plane")