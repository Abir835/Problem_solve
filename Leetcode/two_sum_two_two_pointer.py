nums = [2, 7, 11, 15]
target = 18

l = 0
r = len(nums) - 1

while l < r:
    total = nums[l] + nums[r]
    if total == target:
        print(l+1, r+1)
        break

    elif total > target:
        r -= 1

    else:
        l += 1
