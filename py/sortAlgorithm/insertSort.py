def insertSort(L):
    for x in range(0, len(L)):
        minIndex = x;
        for y in range(0, x):
            if(L[minIndex]<L[y]):
                temp=L[minIndex]
                L[minIndex]=L[y]
                L[y]=temp

    return L