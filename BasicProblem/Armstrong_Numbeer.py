num = int(input())
order = len(str(num))

result = 0
temp = num
while temp > 0:
    digit = temp % 10
    result += digit ** order
    temp = temp // 10

if num == result:
    print(num)
else:
    print("not a number")