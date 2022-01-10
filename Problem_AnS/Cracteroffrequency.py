n = input()
x = set()
result = " "
for i in n:
    if i not in x:
        x.add(i)
        result = result + str(n.count(i)) + i
print(result)
