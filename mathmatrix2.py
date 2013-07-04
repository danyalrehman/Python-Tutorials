__author__ = 'danyalrehman'

def mathmatrixmultiplier(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1 ,e2 ,e3, f1 ,f2, f3):
    """ the aim of this function is to take in a matrix with
    3 rows. Where the first row is 'a', the next row 'b' and the
    last row 'c', and then multiplies it to the matrix with row
    'd', 'e' and 'f' respectively.
    """

    newa1 = (a1 * d1) + (a2 * e1) + (a3 * f1)
    newa2 = (a1 * d2) + (a2 * e2) + (a3 * f2)
    newa3 = (a1 * d3) + (a2 * e3) + (a3 * f3)
    print newa1, newa2, newa3
    newb1 = (b1 * d1) + (b2 * e1) + (b3 * f1)
    newb2 = (b1 * d2) + (b2 * e2) + (b3 * f2)
    newb3 = (b1 * d3) + (b2 * e3) + (b3 * f3)
    print newb1, newb2, newb3
    newc1 = (c1 * d1) + (c2 * e1) + (c3 * f1)
    newc2 = (c1 * d2) + (c2 * e2) + (c3 * f2)
    newc3 = (c1 * d3) + (c2 * e3) + (c3 * f3)
    print newc1, newc2, newc3

    print
    print

    firstrowopa1 = float(newa1) / newa1
    firstrowopa2 = float(newa2) / newa1
    firstrowopa3 = float(newa3) / newa1

    secondrowopb1 = float(newb1) - (newb1 * firstrowopa1)
    secondrowopb2 = float(newb2) - (newb1 * firstrowopa2)
    secondrowopb3 = float(newb3) - (newb1 * firstrowopa3)

    thirdrowopc1 = float(newc1) - (newc1 * firstrowopa1)
    thirdrowopc2 = float(newc2) - (newc2 * firstrowopa2)
    thirdrowopc3 = float(newc3) - (newc3 * firstrowopa3)

    

# row reducer

    secondrowopb11 = secondrowopb1 / secondrowopb2
    secondrowopb12 = secondrowopb2 / secondrowopb2
    secondrowopb13 = secondrowopb3 / secondrowopb2

    firstrowopa11 = firstrowopa1 - (firstrowopa2 * secondrowopb11)
    firstrowopa12 = firstrowopa2 - (firstrowopa2 * secondrowopb12)
    firstrowopa13 = firstrowopa3 - (firstrowopa2 * secondrowopb13)

    thirdrowopc11 = thirdrowopc1 - (thirdrowopc2 * secondrowopb11)
    thirdrowopc12 = thirdrowopc2 - (thirdrowopc2 * secondrowopb12)
    thirdrowopc13 = thirdrowopc3 - (thirdrowopc2 * secondrowopb13)

    thirdrowopc21 = thirdrowopc11 / thirdrowopc13
    thirdrowopc22 = thirdrowopc12 / thirdrowopc13
    thirdrowopc23 = thirdrowopc13 / thirdrowopc13

    firstrowopa21 = firstrowopa11 - (firstrowopa13 * thirdrowopc21)
    firstrowopa22 = firstrowopa12 - (firstrowopa13 * thirdrowopc22)
    firstrowopa23 = firstrowopa13 - (firstrowopa13 * thirdrowopc23)


    secondrowopb21 = secondrowopb11 - (secondrowopb13 * thirdrowopc21)
    secondrowopb22 = secondrowopb12 - (secondrowopb13 * thirdrowopc22)
    secondrowopb23 = secondrowopb13 - (secondrowopb13 * thirdrowopc23)

    print firstrowopa21, firstrowopa22, firstrowopa23
    print secondrowopb21, secondrowopb22, secondrowopb23
    print thirdrowopc21, thirdrowopc22, thirdrowopc23

    print
    print

    print int(firstrowopa21), int(firstrowopa22), int(firstrowopa23)
    print int(secondrowopb21), int(secondrowopb22), int(secondrowopb23)
    print int(thirdrowopc21), int(thirdrowopc22), int(thirdrowopc23)

print mathmatrixmultiplier(123,32,2,14,1,5,43,4,43,54,35,436,232,4,13,123,432,543)