def getMinMax(a, n):
    min = a[0]
    for i in range(1, n):
        if min > a[i]:
            min = a[i]

    max = a[0]
    for i in range(1, n):
        if max < a[i]:
            max = a[i]

    return [min, max]


print(getMinMax([-1,1, 100, 2, 3, 4, 5, 10000], len([-1, 1, 100, 2, 3, 4, 5, 10000])))
