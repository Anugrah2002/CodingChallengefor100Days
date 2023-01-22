def series2():
    n = int(input("enter the digit : "))
    a = 0.5
    for i in range (0,n-1):
        b = a*3
        a=b
        print(a)

series2()

# 0.5,1.5,4.5,13.5,29.5

# 0   1   3    9    16