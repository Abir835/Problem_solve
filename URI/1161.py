n = int(input())
sum1 = 0
for i in range(n):
    x = int(input())
    c = int(x / 2)
    d = 0
    for j in range(1, c + 1):
        if x % j == 0:
            d = d + j
    if d == x:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))
