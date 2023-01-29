nums = [0, 1, 2, 0, 13]

l = 0
for r in range(len(nums)):
    if nums[r]:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1


print(nums)
