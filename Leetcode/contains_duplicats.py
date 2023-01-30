def containsDuplicate(nums):
    # count_val = {}
    # for data in nums:
    #     if data in count_val:
    #         count_val[data] += 1
    #     else:
    #         count_val[data] = 1
    #
    # for data_ in count_val.values():
    #     if data_ > 1:
    #         return True
    #     else:
    #         data_ += 1
    # return False

    num2 = set(nums)
    l1 = len(nums)
    l2 = len(num2)
    if l1 != l2:
        return True
    else:
        return False


print(containsDuplicate([1, 2, 3, 4,1]))
