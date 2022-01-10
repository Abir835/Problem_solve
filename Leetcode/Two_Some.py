value = []
n = int(input())
for i in range(n):
    b = int(input())
    value.append(b)
target = int(input())
# print(value)
A = []
for i in range(len(value)):
    for j in range(i + 1, len(value)):
        if target == value[j] + value[i]:
            A.append(i)
            A.append(j)

print(A)
