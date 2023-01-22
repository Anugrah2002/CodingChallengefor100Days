def check_kaprekar(a = 297):  
    e= []
    strs = str(a)
    d = len(strs)
    if d == 3:
        a =a&10
        e.append(a)
        print(e)


check_kaprekar()