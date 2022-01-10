while True:
    a = 0
    b = 0
    while b < 2:
        n = float(input())
        if 0 <= n <= 10:
            b = b + 1
            a = a + n
        else:
            print("nota invalida")
    print("media = %.2f" % (a / 2))
    t = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        t = int(input())
        if t == 1 or t == 2:
            break
    if t == 2:
        break
