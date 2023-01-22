def arraySpecialProduct():
    a = [1,2,3,4,5]
    b = []
    c = 1
    for i in a :
        c = c*i
    for i in a:
        d = c //i
        b.append(d)
    print(b)

arraySpecialProduct()
