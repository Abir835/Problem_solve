# x, y = list(map(int, input().split()))
# if x > y:
#     x, y = y, x
# for i in range(1, y, 3):
#     a = i
#     b = i + 1
#     c = i + 2
#     print("{} {} {}".format(a, b, c))

# X, Y = input().split()
# X = int(X)
# Y = int(Y)
# count = 0
# for i in range(1, Y + 1):
#     print(i, end=" ")
#     count += 1
#     if count == X:
#         print(" ")
#         count = 0


# n1, n2 = list(map(int, input().split()))
# cont = 1
# for i in range(1, (int((n2 / n1)) + 1)):
#     r = ""
#     for y in range(n1):
#         r += str(cont) + " "
#         cont += 1
#     print(r[:-1])
