

class Solution(object):
    def kids_withCandies(self, candies, extraCandies):
        n = sorted(candies)
        last_ = n[len(n)-1]
        res_ = []
        for i in candies:
            x = i+extraCandies
            if x >= last_:
                res_.append(True)
            else:
                res_.append(False)
        return res_

obj = Solution()
print(obj.kids_withCandies([2,3,5,1,3], 3))