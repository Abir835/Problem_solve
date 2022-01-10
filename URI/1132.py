sumx = 0

x = int(input())
y = int(input())
t = x
if x > y:
    x = y
    y = t
while x <= y:
    if x % 13 != 0:
        sumx = sumx + x
    x = x+1
print(sumx)
