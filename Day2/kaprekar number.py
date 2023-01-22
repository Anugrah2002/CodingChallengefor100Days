def check_kaprekar():  
    e= 0
    a = 123497
    strs = str(int)
    d = len(strs)
    for i in range (0,d-1) :
        c = a%10
        e =e+c
        a =a//10
    print(e)
    if e >= 0 and e< 10:
        print(e)
    else:
        print('soory')
        # check_kaprekar(a=e)



check_kaprekar()
  