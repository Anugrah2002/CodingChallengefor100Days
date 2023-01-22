def rearrangePositiveAndNegatuveIntegres():
    a =[]
    neg = []
    pos = []
    result = []
    n = int(input('enter the array size : '))
    for i in range(0, n):
        b = int(input('enter the '+ str(i) +' number of array : '))
        a .append(b)
    for i in a:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    size  = len(neg)

    print(neg)
    print(pos)


    # print(neg)
    # print(neg)

    # for i in range(0,n):




rearrangePositiveAndNegatuveIntegres()