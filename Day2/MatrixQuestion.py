def largestElementInTheMatrixColumn():
    matrix =[]
    n = int(input('Enter the the number of rows and columns : '))
    for i in range(0,n):
        a = []
        for j in range(0,n):
            a.append(int(input('enter the matrix elements : ')))
        matrix.append(a)
    print('your matrix is : ')
    for i in range(0,n):
        for j in range(0,n):
            print(matrix[i][j], end= " ")
        print()

    print('largest number among rows are : ')
    for i in range(0,n):
        s = 0
        for j in range(0,n):
            if (matrix[i][j] > s ):
                s = matrix[i][j]
        
        print(s)



largestElementInTheMatrixColumn()