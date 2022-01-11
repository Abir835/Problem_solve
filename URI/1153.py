n = int(input())
fact = 1
if 0 < n < 23:
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
