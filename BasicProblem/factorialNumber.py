def Factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


x = int(input("Enter Number.....:"))
result = Factorial(x)
print("Factorial Number:", result)
