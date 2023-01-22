def partition(a, low, high):
    pivot = a[0]
    print(pivot)
    low = low+1
    for i in range(low,high):
        if a[i] > pivot:
            print(a[i])
            for j in range(high,low):
                print(j)





def quickSort():
    a = [2,4,3,9,1,4,8,7,5,6]
    n = len(a)
    low = 0
    high = n
    pi = partition(a,low, high)
    pass


quickSort()
