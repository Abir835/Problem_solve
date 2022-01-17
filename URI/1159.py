
while True:
    sum1= 0

    x = int(input())

    if x == 0:
        break

    if x % 2 != 0:
        x = x+1

    for i in range(5):
        sum1 = sum1 + x
        x = x+2

    print(sum1)

