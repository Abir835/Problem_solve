a = int(input())

for i in range(a):
    x, y = list(map(int, input().split()))
    if y == 0:
        print("divisao impossivel")
    else:
        print("%.1f" % (x / y))


