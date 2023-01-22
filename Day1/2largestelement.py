def secondLargestelement():
    a = [12,35,1,10,34,1]
    n = 6
    larg = 0
    second_largest = 0
    for i in a:
        if i > larg:
            larg = i
    for i in a:
        if i <larg and i>second_largest :
            second_largest = i

    print(second_largest)
secondLargestelement()

