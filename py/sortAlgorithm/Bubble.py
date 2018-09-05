def Bubble(L):
    for x in range(0, len(L)):
        for y in range(x, len(L)):
            if ( L[x] > L[y] ):
                temp = L[x]
                L[x] = L[y]
                L[y] = temp

    return L