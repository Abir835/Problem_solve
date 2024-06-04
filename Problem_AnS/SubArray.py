def sub_array(arr):
    data = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n + 1):
            data.append(arr[i:j])
    max_sum = float('-inf')
    for sub in data:
        cur_sum = sum(sub)
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum

    # if not arr:
    #     return 0  # In case the input array is empty
    #
    # max_sum = current_sum = arr[0]
    #
    # for num in arr[1:]:
    #     current_sum = max(num, current_sum + num)
    #     max_sum = max(max_sum, current_sum)
    #
    # return max_sum


#     max_sum = arr[0]
#     cur_sum = 0
#     for i in arr:
#         if cur_sum < 0:
#             cur_sum = 0
#         cur_sum += i
#
#         if cur_sum > max_sum:
#             max_sum = cur_sum
#         else:
#             max_sum = max_sum
#
#     return max_sum
#
#
print(sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
