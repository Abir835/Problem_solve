a = 0
b = 0
c = 0

n = int(input())
for i in range(1, n+1):
    a = i
    b = i * a
    c = i * b

    print("{0} {1} {2}".format(a, b, c))

    i = i + 1
