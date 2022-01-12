sum1 = 0
b = 1

for i in range(1, 40, 2):
    n = i / b
    sum1 = sum1 + n
    b = b * 2
print("{0:.2f}".format(sum1))
