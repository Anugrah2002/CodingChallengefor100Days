def targetValue():
    targetvalue = 100

    a = int(input("enter the number : "))
    count = 1
    while a<targetvalue:
        b = int(input("enter the  number : "))
        a = a+b

        count +=1
    print(count)


targetValue()