# t = int(input())
#
# arr = []
#
# for i in range(t):
#     arr.append(i+1)
#
# n = list(map(int, input().split()))
#
# for i in arr:
#     if i not in n:
#         print(i)
#


t = int(input())

arr = set(range(1, t + 1))
n = set(map(int, input().split()))
missing_numbers = arr - n
for i in missing_numbers:
    print(i)