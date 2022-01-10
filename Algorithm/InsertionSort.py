def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = item


arr = [1, 4, 5, 7, 1, 2, 3]
InsertionSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")

# Descending Order
# def InsertionSort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         item = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] < item:
#             arr[j + 1] = arr[j]
#             j = j - 1
#
#         arr[j + 1] = item
#
#
# arr = [1, 4, 5, 7, 1, 2, 3]
# InsertionSort(arr)
# for i in range(len(arr)):
#     print(arr[i], end=" ")
