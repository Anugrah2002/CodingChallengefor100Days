def Check_palindrome():
    lists = []
    n = int(input('enter the number : '))
    binary = bin(n).replace("0b", "")
    print(binary)
    lens =len(binary)

    for i in binary:
        lists.append(i)
    print(lists)
    c= list(reversed(binary))
    print(c)
    if lists == c:
        print('it is palindrome')
    else:
        print('it is not palindrome')


Check_palindrome()