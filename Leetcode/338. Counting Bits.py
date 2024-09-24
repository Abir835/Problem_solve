class Solution(object):
    def countBits(self, n):

        list_ = [0] * (n + 1)
        for x in range(0, n + 1):
            list_[x] = list_[x // 2] + (x % 2)

        return list_

obj = Solution()
print(obj.countBits(7))