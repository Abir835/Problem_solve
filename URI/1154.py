count = 0
sum1 = 0
while True:
    n = int(input())
    if n < 0:
        break
    else:
        sum1 = sum1 + n
        count += 1

print("{0:.2f}".format(sum1/count))

