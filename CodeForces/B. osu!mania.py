t = int(input())

for _ in range(t):
    n = int(input())
    list_ = []

    for i in range(n):
        inp = input()

        for j in range(len(inp)):
            if inp[j] == "#":
                list_.append(j + 1)

    for j in range(len(list_) -1, -1, -1):
        print(list_[j], end=" ")

    print()
