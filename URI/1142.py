a, b, c = 1, 2, 3

n = int(input())

for i in range(n):
    print("{0} {1} {2} PUM".format(a, b, c))

    d = c+2
    a = d
    b = a+1
    c = a+2

    i = i + 1
