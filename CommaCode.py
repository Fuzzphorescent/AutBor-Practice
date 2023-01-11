def commaCode(L):
    n = length(L)
    for i in range(n):
        x = input()
        L.append(x)

    if n != 0:
        if n != 1:
            for i in range(n-1):
                print(str(L[i]) + ', ', end = '')
            print('and ', end = '')
        print(str(L[0]))
        