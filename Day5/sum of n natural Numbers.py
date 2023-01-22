n = int(input('enter the number : '))
def nNaturalNumbers(n):
    if n == 1:
        return 1
    else:
        return n + nNaturalNumbers(n-1)

print(nNaturalNumbers(n))


# using recursion