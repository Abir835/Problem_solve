n = list(map(int, input().split()))
z = [1, 2, 3]
x = []
for i in z:
    if i in n:
        pass
    else:
        x.append(i)

for i in x:
    print(i, end=" ")
