n = int(input())
count = 0
list1 = []
a, b = 0, 1
if 0 < n < 46 and n > 1:
    while count < n:
        list1.append(a)
        nth = a + b
        a = b
        b = nth
        count = count + 1

z = (str(list1[0:n]).replace(",", ""))
print(z.strip('[]'))
