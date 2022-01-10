x = input()
z_list = x.split()
m = list(z_list)
a = int(m[0])
n = int(m[-1])
sum1 = 0
while n == 0 and a < 0:
    n = int(input())
for i in range(n):
    sum1 = sum1+a+i
print(sum1)
