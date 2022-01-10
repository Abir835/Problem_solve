n = float(input())
if n >= 0 and n <= 400:
    a = n * 0.15
    b = n + a
    c = 15
elif n >= 400.01 and n <= 800.00:
    a = n * 0.12
    b = n + a
    c = 12
elif n >= 800.01 and n <= 1200.00:
    a = n * 0.10
    b = n + a
    c = 10
elif n >= 1200.01 and n <= 2000.00:
    a = n * 0.07
    b = n + a
    c = 7
elif n > 2000:
    a = n * 0.04
    b = n + a
    c = 4
print(f"Novo salario: {b:.2f}")
print(f"Reajuste ganho: {a:.2f}")
print(f"Em percentual: {c} %")

