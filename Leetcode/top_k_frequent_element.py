import collections
from typing import List


class Solution:

    def fun(self, nums):
        return nums[1]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_map = collections.Counter(nums)
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # for num in nums:
        #     freq_map[num] += 1
        sorted_freq_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        print(sorted_freq_map)
        print(sorted_freq_map[:k])

        # Extract the keys (numbers) of the top k frequent elements
        top_k_elements = [key for key, _ in sorted_freq_map[:k]]

        return top_k_elements


obj = Solution()
obj.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
