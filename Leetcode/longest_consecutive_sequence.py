from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = sorted(set(sorted(nums)))
        if len(new_list) <= 0:
            return 0
        count = 1
        max_count = 1
        for i in range(1, len(new_list), 1):
            if new_list[i - 1] == new_list[i] - 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1

        max_count = max(count, max_count)
        return max_count


obj = Solution()
print(obj.longestConsecutive([2, 3, 3, 4, 4, 5, 5, 6, 10, 11, 12]))
