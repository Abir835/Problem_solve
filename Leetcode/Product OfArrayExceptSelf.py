def productExceptSelf(nums):
    # n = len(arr)
    # arr_new = []
    # for i, j in enumerate(arr):
    #     arr.pop(i)
    #     new_data = 1
    #     for data in arr:
    #         new_data *= data
    #     arr_new.append(new_data)
    #     arr.insert(i, j)
    # return arr_new

    # res = [1] * (len(nums))
    #
    # prefix = 1
    # for i in range(len(nums)):
    #     res[i] = prefix
    #     prefix *= nums[i]
    #
    # postfix = 1
    # for i in range(len(nums) - 1, -1, -1):
    #     res[i] *= postfix
    #     postfix *= nums[i]
    #
    # return res
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n

    for i in range(n):
        j = -i - 1
        l_arr[i] = l_mult
        r_arr[i] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]

    return [l * r for l, r in zip(l_arr, r_arr)]


print(productExceptSelf([-1, 1, 0, -3, 3]))
