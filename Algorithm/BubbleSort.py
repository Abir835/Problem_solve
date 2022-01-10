def BubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [1, 5, 2, 4, 9]
BubbleSort(arr)

print('Bubble Sort')
for i in range(len(arr)):
    print(arr[i], end=' ')

# Descending Order
# def BubbleSort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [1, 5, 2, 4, 9]
# BubbleSort(arr)
#
# print('Bubble Sort')
# for i in range(len(arr)):
#     print(arr[i], end=' ')

