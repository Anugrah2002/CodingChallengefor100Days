def nthPrimeNumber ():
    n =10
    # n = int (input('enter the number : '))
    count = 0
    num = 3
    for i in range(2,40):
        if num % i !=0:
            print(num)
            print(i)
            count = count + 1
            if count ==n:
                print(num)
        else:
            num = num +1

            
             
    # for i in range(2, 40):
    #     if num % i == 0:
    #         num = num+1
    #     else: 
    #         print('ooo')
    #         count +=1
    #         if count == n:
    #             print(x) 
    #             break



nthPrimeNumber()
