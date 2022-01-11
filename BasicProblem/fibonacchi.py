n = int(input())

a, b = 0, 1
count = 0
if n > 0 and n > 1:
    while count < n:
        print(a)
        nth = a+b
        a = b
        b = nth
        count = count+1
