def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


num = int(input())
if num > 0:
    print(factorial(num))
