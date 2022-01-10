n = int(input())
x = [int(i) for i in input().split()]

x.sort(reverse=True)

for i in range(n):
    if x[0] == x[i]:
        continue
    else:
        print(x[i])
        break
