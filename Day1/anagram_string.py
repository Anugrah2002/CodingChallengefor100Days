def anagram():
    n1 = str(input('enter the first string : '))
    n2 = str(input('enter the second string : '))
    if len(n1) != len(n2):
        print('it is not anagram')
    else:
        
        if sorted(n1) == sorted(n2):
            print('it is anagram')
        else:
             print('it is not')
                


anagram()