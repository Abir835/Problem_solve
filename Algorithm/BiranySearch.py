def BinarySearch(array, left, right, find):
    # check left smaller or equal
    while left <= right:
        # find mid value
        mid = left + (right - left) // 2
        if array[mid] == find:
            return mid
        # if mid less the find value then mid +1
        elif array[mid] < find:
            left = mid + 1
        # else mid -1
        else:
            right = mid - 1
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
find = 10
result = BinarySearch(array, 0, len(array) - 1, find)

if result != 1:
    print("Index No:", result)
else:
    print("Not Find")
