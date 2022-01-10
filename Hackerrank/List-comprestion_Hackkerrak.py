x = int(input())
y = int(input())
z = int(input())

n = int(input())
l = []
ls = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k == n:
                continue
            else:
                ls = [i, j, k]
                l.append(ls)

print(l)
