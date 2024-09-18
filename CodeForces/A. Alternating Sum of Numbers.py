t = int(input())

for _ in range(t):

    n = int(input())

    sequence = list(map(int, input().split()))

    alternating_sum = 0

    for i in range(n):
        if i % 2 == 0:
            alternating_sum += sequence[i]
        else:
            alternating_sum -= sequence[i]

    print(alternating_sum)


