# while True:
#     n = int(input())
#     if n == 0:
#         break
#     for i in range(1, n + 1):
#         print(i, end=" ")
#     print('\n')


while True:
    a = int(input())
    r = ''
    if a == 0:
        break
    for i in range(1, a + 1):
        r += str(i) + " "
    print(r[:-1])

