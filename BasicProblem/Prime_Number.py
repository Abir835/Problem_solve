lower = int(input())
higher = int(input())
x = []
for num in range(lower, higher + 1):
    if num > 1:
        if num % 2 == 0:
            continue
        else:
            x.append(num)

for i in x:
    print(i, end=" ")
