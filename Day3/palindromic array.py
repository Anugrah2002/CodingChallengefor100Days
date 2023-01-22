def PalinArray(arr ,n):
    rev = 0
    for i in arr:
        print(i)
        temp =i
        while (temp!=0):
            rev =(rev*10)+temp%10
            temp = temp //10
        if rev == i:
            return 1
        else:
            return 0
