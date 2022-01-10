def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


rec = fact(5)
print(rec)
