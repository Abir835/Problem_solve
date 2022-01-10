n = int(input())
arr = []
even = []
odd = []
unique = []
for i in range(0, n):
    temp = int(input())
    arr.append(temp)
print("Serial Number....")
print(arr)
print("Decending Number....")
for i in range(1, len(arr) + 1):
    print(arr[-i])

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even Number....")
print(even)
print("Odd Number....")
print(odd)
# unique = []
# for i in range(1, len(arr)):
#
#     if arr[i] == arr[i-1]:
#         continue
#     else:
#         unique.append(arr[i])
# print("Unique Number....")
# print(unique)

for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)