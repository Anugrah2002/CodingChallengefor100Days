n = int(input('enter the number : '))
def nthFibbonacciSeries(n):
    if n <= 1:
        return n
    else:
        return nthFibbonacciSeries(n-1) + nthFibbonacciSeries(n-2)




print(nthFibbonacciSeries(n))

# usnig recursion