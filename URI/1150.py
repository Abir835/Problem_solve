a = int(input())


while True:
    b = int(input())
    if b > a:
        break

sum1 = a
counter = 1
while sum1 < b:
    sum1 = sum1 + a + counter
    counter = counter + 1

print(counter)