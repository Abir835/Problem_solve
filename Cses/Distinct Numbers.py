n = int(input())
values = sorted(map(int, input().split()))
distinct_count = 1

for i in range(1, n):
    if values[i] != values[i - 1]:
        distinct_count += 1
print(distinct_count)
