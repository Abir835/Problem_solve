a = [1, 2, 3, 5, 7]
b = [1, 4, 2, 3]
count = 0
x = []
for i in range(len(a)):
    if a[i] in b:
        continue
    else:
        x.append(a[i])

for i in range(len(b)):
    if b[i] in a:
        continue
    else:
        x.append(b[i])
print(x)
# for i in a:
#     if i not in b:
# print(i)
