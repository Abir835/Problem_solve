# value = []
#
#
# def LinearSearch(List, x, y):
#     flag = False
#     for i in range(0, y):
#         if List[i] == x:
#             flag = True
#             value.append(i)
#     if flag:
#         return 1
#     else:
#         return -1
#
#
# L = [1, 2, 2, 4, 5, 8, 9, 8]
# y = len(L)
# x = int(input())
# result = LinearSearch(L, x, y)
#
# if result == 1:
#     for i in value:
#         print(i)
# else:
#     print("Not Find")

def linearSearch(array, n, x):

    # Going through array sequentially
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = int(input())
n = len(array)
result = linearSearch(array, n, x)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)
